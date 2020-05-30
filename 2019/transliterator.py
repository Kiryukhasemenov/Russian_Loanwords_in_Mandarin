# -*- coding: utf-8 -*-

from pymorphy2 import MorphAnalyzer
import re
import pandas as pd 

table=pd.read_csv('translit_version2.csv',sep=';')

class Transliterator:
    
    def __init__(self, input_word, table):
        '''
        Args: 
            input word: str, string with Russian characters
            table: .csv table with Xinhua prescriptions
        '''
        self.input_word = input_word
        self.table = table
        self.syllables = self.chunker(self.input_word)
        self.sex = self.feminine_checker(self.input_word)
        self.output_word = self.transliterate()
    
    def __repr__(self):
        return self.output_word
    
    __str__ = __repr__
    
    def feminine_checker(self, w): 
        '''
        Check if the word is feminine. Necessary for some variants of hieroglyphs
        Args:
            w: str, input Russian word
        Returns:
            sex: str, 'M' or 'F' - gender of a word
        '''

        morph = MorphAnalyzer()
        w = self.input_word.split(' ')[0]
        ana = morph.parse(w)[0]
        gram = str(ana.tag).split(',')
#        print(gram)
        try:
            if 'femn' in gram[2]:
                sex = 'F'
            else:
                sex = 'M'
        except:
            if w[-1] == 'а' or w[-1] == 'я':
                sex = 'F'
            else:
                sex = 'M'
        self.sex = sex
        return self.sex
    
    def cleaner(self, w_old):
        """
        Cleans input string from non-Russian characters
        Args:
            w_old: Russian input string
        Returns:
            w_new: Russian string without anything except Russian alphabet or whitespaces
        """
        w_new = re.sub('[\(\)]', '', w_old)
        w_new = re.sub('[^А-Яа-яЁё ]', 'ъ', w_new)
        w_new = re.sub(' ', '  ', w_new)
        return w_new
    
    def ch_t_checker(self, seq):
        """
        Changes input string according to note 1 in transliteration table
        Args:
            seq: Russian string
        Returns
            seq: changed string
        """
        seq = re.sub(r'чт', r'шт', seq)
        return seq

    def mp_mb_checker(self, seq):
        """
        Changes input string according to note 1 in transliteration table
        Args:
            seq: Russian string
        Returns
            seq: changed string
        """
#        print('input ' + seq)
        seq = re.sub(r'([ёуеыаоэяию])м(п|б)',r'\1н\2',seq)
#        print('output ' + seq)
        return seq

    def beginning_liquid_checker(self, translit):
        """
        Changes output string according to note 1 in transliteration table
        Args:
            seq: preliminary Chinese string
        Returns
            seq: changed Chine string
        """
        tr_new = re.sub(r'(\A|·)尔', r'\1勒', translit)
        return tr_new
    
    def yotated_checker(self, seq):
        """
        Changes input string in order to unify the occurences of yotated vowels
        Args:
            seq: Russian string
        Returns
            seq: changed string
        """
        seq = re.sub(r'([йцкнгшщзхфвпрлджчсмтб])(й(а|у|э))', r'\1ь\2', seq)
        seq = re.sub(r'(\A| |[ьъ])йа', r'\1я', seq)
        seq = re.sub(r'(\A| |[ьъ])йу', r'\1ю', seq)
        seq = re.sub(r'(\A| |[ьъ])йэ', r'\1е', seq)
        return seq

    def gk_g_checker(self, seq):
        """
        Changes input string according to note 1 in transliteration table
        Args:
            seq: Russian string
        Returns
            seq: changed string
        """
        seq = re.sub(r'гк', r'хк', seq)
        return seq

    def geminates_checker(self, s):
        """
        Changes input string in order to consider geminates as unique consonants
        Args:
            s: Russian string
        Returns
            s: changed string
        """
        s = re.sub(r'([йцкгшщзхфвпрлджчсмтб])\1+', r'\1', s)
        s = re.sub(r'н{2}([йцкгшщзхфвпрлджчсмтб ])', r'н\1', s)    
        return s

    def beginning_checker(self, translit):
        """
        Changes output string according to note 1 in transliteration table
        Args:
            translit: preliminary Chinese string
        Returns
            translit: changed Chinese string
        """
        tr_new = re.sub(r'(\A|·)夫', r'\1弗', translit)
        tr_new = re.sub(r'(\A|·)耶', r'\1叶', tr_new)
        return tr_new

    def yo_and_n_checker(self, translit):
        """
        Changes input in order to unify the occurrences of the letter ё 
                and the following consonants (not codified in Xinhua prescriptions)
        Args:
            seq: Russian string
        Returns
            seq: changed string
        """
        tr_new = re.sub(r'ёнь', r'ё\'нь', translit)
        tr_new = re.sub(r'ён([йцкнгшщзъфвпрлджчсмтб])', r'он\'\1', tr_new)
        return tr_new

    def initial_finder(self, seq, ins):
        """
        Finds appropriate initial in the beginning of the string
        Args:
            seq: str, the (rest of the) input Russian word
            ins: list, list of all possible initials (row names in table)
        Returns:
            initial: str, the initial for the next syllable
            len_init: int, number of symbols to cut off to get the final
        """
#        print('call initial_finder, input = '+seq)
        letter=seq[0]
        if letter in ins:
            if letter in ['д','т','ц','с']:
                next_letter=seq[:2]
                if next_letter in ins:
                    initial=next_letter
                    len_init=2
                else:
                    initial=letter
                    len_init=1
            else:
                initial=letter
                len_init=1    
        else:
            initial='_'
            len_init=0
#        print(initial)
        return initial, len_init

    def final_finder(self, seq, init_length, fs):
        """
        Finds appropriate final for the existing initial in the beginning of the string
        Args:
            seq: str, the (rest of the) input Russian word
            init_length: int, number of symbols to delete in order to start searching final
            fs: list, list of all possible finals (column names in table)
        Returns:
            final: str, the final for the syllable
            len_final: int, number of symbols to cut off to get the next syllable
        """
#        print('call final_finder, input = '+seq)
        where_final=seq[init_length:]
        if len(where_final)>0:
            letter=where_final[0]
            if letter in fs:
                if len(where_final) > 1:
                    yo = where_final[0] == 'ё'
                    o = where_final[0] == 'о'
                    if yo:
                        final = where_final[0]
                        len_final = 1
                    elif o:
                        if where_final[1] == 'й':
                            final = where_final[:2]
                            len_final = 2
                        else:
                            final = where_final[:1]
                            len_final = 1
                    elif where_final[1] in ['й','и','о','ю','у']:
                        if where_final[:2] in fs:
                            final=where_final[:2]
                            len_final = 2
                        else:
                            final = letter
                            len_final = 1
                    elif where_final[1] == 'н':
#                        print('second letter = n')
#                        print('check')
                        if len(where_final) > 2:
                            if where_final[2] == 'ь' or where_final[2] == 'г':
#                                print('third letter = ь or г')
                                soft_sign = where_final[2] == 'ь'
                                g = where_final[2] == 'г'
                                if where_final[:3] in fs:
#                                    print('now find out if its rather initial')
                                    if len(where_final) > 3 and soft_sign:
                                        final = where_final[:3]
                                        len_final = 3
                                    elif len(where_final) > 3 and g:
                                        if where_final[3] in ['а','о','у','ы','э','я','ё','ю','и','е','ь']:
                                            final = where_final[:2]
                                            len_final = 2
                                        else:
                                            final = where_final[:3]
                                            len_final = 3
                                    else:
                                        final = where_final[:3]
                                        len_final = 3
                                else:
#                                    print('no, theres no such combination of 3 symbols')
                                    final = where_final[:2]
                                    len_final = 2
                            elif where_final[2] in ['а','о','у','ы','э','я','ё','ю','и','е']:
#                                print('third letter = vowel')
                                final = where_final[:1]
                                len_final = 1
                            else:
                                final=where_final[:2]
                                len_final = 2

                        else:
                            final=where_final[:2]
                            len_final = 2

                    else:
                        final=where_final[0]
                        len_final = 1
                else:
                    final=where_final[0]
                    len_final = 1
            elif where_final[:2] == 'йо':
                final = where_final[:2]
                len_final = 2
            else:
#                print('no such symbol, whitespace or Ъ')
                if letter == ' ':
                    final='_'
                    len_final = 1
                elif letter == 'ъ':
                    final = '_'
                    len_final = 1
                else:
                    final = '_'
                    len_final = 0
        else:
            final='_'
            len_final = 0            
#        print(final)
        return final, len_final

    def chunker(self, w):
        """
        Chunks the input Russian words into a list of syllables, which contain from initials and finals
        Args:
            w: str, input Russian word
        Returns:
            syls: list, list of syllables, each element consists of two str objects - initial and final
        """
#        print('call chunker')
        w = self.input_word
        w=w.lower()
        initials=self.table.columns.values.tolist()
        finals=self.table['Unnamed: 0'].tolist()
        w = self.cleaner(w)
        w = self.geminates_checker(w)
#        print('now go mb mp')
        w = self.mp_mb_checker(w)
        #print('the result is: '+w)
        w = self.gk_g_checker(w)
        w = self.ch_t_checker(w)
        w = self.yotated_checker(w)
#        print('the result is: '+w)
        syls = []
        counter = True
        while len(w) > 0 and counter:
            s_len = len(syls)
            initial, len_init = self.initial_finder(w, initials)
            final, len_fin = self.final_finder(w, len_init, finals)
            len_syllable = len_init+len_fin
            final_idx=finals.index(final)
            syllable = [initial, final, final_idx]
            w_old = w
            w = w[len_syllable:]
            syls.append(syllable)
            if len(w_old) == len(w):
#                print('we got into a hole')
                counter = False
        if counter == False:
            syls = []
        return syls
    
    def transliterate(self):
        """
        Transforms the list of syllables into Chinese characters
        Args:
            self.syllables: list, list of syllables
            self.sex: str, sex of an object 
                    (necessary for character choice by note 2 in transliteration table)
        Returns:
            word: str, final string of Chinese characters
        """
#        print('call transliterator, input = '+str(self.syllables))
        word = ''
        if len(self.syllables) == 0:
            word = 'U'
            return word
        else:
            for s in self.syllables:
                i, f = s[0], s[-1]
#                print(i, f)
                try:
                    variants = self.table[i][f].split(' ')
                except:
                    word = 'N'
                    return word
                if len(variants) > 1:
                    if self.sex == 'M':
                        word += variants[0]
                    else:
                        word += variants[1]
                else:
                    word += variants[0]
        word = self.beginning_checker(word)
        word = self.beginning_liquid_checker(word)
        word = re.sub(r'··', r'·', word)
        return word
        