import sublime
import sublime_plugin
import os
import shutil

class BckCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#self.view.insert(edit, 0, "Hello, World!")
         #view.run_command('save')
		 file_path = self.view.file_name()
		 file_base_name = os.path.basename(file_path)
		 dir_name = os.path.dirname(file_path)
		 target_file = file_base_name + '.bck'
		 full_target =  os.path.join(dir_name, target_file)
		 #self.view.insert(edit, 0, full_target)
		 shutil.copyfile(file_path,full_target)
