import sublime
import sublime_plugin
import os
import re
import shutil

class IfcomCommand(sublime_plugin.TextCommand):
      def run(self, edit):
        for region in self.view.sel():
            print('My current region ' + str(region))
            all_begin_end_instances = self.view.find_all('(begin|end)')
            end_search = 0
            my_output_list = []
            list_index = 0
            #searching matching end
            for item in all_begin_end_instances:
                if(item.a > region.a):
                    print('WE HAVE FOUND A PLACE ' + str(item))
                    break
                print(item)
                print(self.view.substr(item))
                end_search = end_search + 1
            my_end = all_begin_end_instances[end_search-1]
            print('OUR END AT ' + str(my_end))
            #searching matching begin
            for item in all_begin_end_instances:
                if(self.view.substr(item) == 'begin'):
                    my_output_list.insert(list_index,item)
                    list_index = list_index + 1
                if( item.a == my_end.a and item.b == my_end.b):
                    break
                if(self.view.substr(item) == 'end'):
                    list_index = list_index - 1
                    my_output_list.pop()
            if(len(my_output_list) != 0):
                print('YOUR BEGIN MATCH ' + str(my_output_list[list_index-1]))
            regex_to_find = '(.*?)(if|else)(.*?)'+ '\n' + '(.*?)(begin)'
            all_ifs_begin_instances = self.view.find_all(regex_to_find)
            for item in all_ifs_begin_instances:
                if(item.contains(my_output_list[list_index-1].a)):
                    if_comment =(' //' + (self.view.substr(item)).lstrip())
                    if('if' in if_comment):
                        if_comment = if_comment.rsplit(')', 1)[0] +')'
                    else:
                        if_comment = if_comment.rsplit('\n', 1)[0]
                    print(if_comment)
                    self.view.replace(edit,region,if_comment)
                
        '''
            if_end = (self.view.substr(self.view.line(region)))
            if_end = re.sub('end.*','end',if_end)
            print(if_end)
            if_begin = '\n' + if_end.replace('end','begin')
            regex_to_find = '(.*?)(if|else)(.*?)' + if_begin + '\n'
            all_begin_instances = self.view.find_all(regex_to_find)
            i=0
            for item in all_begin_instances:
                if(item.a < region.a):
                    last_match_index = item
                    i = i+1
            print('My cursor place ' + str(region))
            print('My last match ' + str(last_match_index))
            fixed_if =(' //' + (self.view.substr(last_match_index)).lstrip()).replace(if_begin,'')
            if('if' in fixed_if):
                fixed_if = fixed_if.rsplit(')', 1)[0] +')'
                self.view.replace(edit,region,fixed_if)
            else:
                fixed_if =(' // else of ' + (self.view.substr(all_begin_instances[i-2]).lstrip()).replace(if_begin,''))
                fixed_if = fixed_if.rsplit(')', 1)[0] +')'
                self.view.replace(edit,region,fixed_if)
            print(fixed_if)
        '''
            