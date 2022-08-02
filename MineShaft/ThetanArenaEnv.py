from .BaseEnv import BaseEnv
import subprocess

class ThetanArenaEnv(BaseEnv):
    def __init__(self, io_mode=IO_MODE.FULL_CONTROL,
                 explore_space=EXPLORE_MODE.FULL):
        super(ThetanArenaEnv, self).__init__()
        
    def step(self, action):
        pass
    
    def reset(self):
        pass
    
    def close(self):
        pass
    
    def _take_action(self, action):
        pass
    
    def _screen_cap(self):
        pass
    
    def _keyboard_input(self, action):
        # scan and find keyboard action
        # key press # self._keyboard_press(ascii_list)
        # key release # self._keyboard_release(ascii_list)
        pass
    
    def _keyboard_press(self, ascii_list):
        pass

    def _keyboard_release(self, ascii_list):
        pass
    
    def _mouse_move(self, action):
        pass
    
    def _mouse_click(self, left, right):
        # scan and find mouse action
        # mouse press #self._mouse_press(left, right)
        # mouse release #self._mouse_release(left, right)
        pass
    
    def _mouse_press(self, left, right):
        pass
    
    def _mouse_release(self, left, right):
        pass
    
    def _start_game(self):
        """
        This is the code for start game
        
        The file path "C:\\Program Files (x86)\\Thetan Arena\\Thetan Arena.exe" 
        and programme name "C:\\Program Files (x86)\\Thetan Arena\\Thetan Arena.exe" 
        is hardcode.
    """
        
        progname = "C:\\Users\\Public\\Desktop\\Thetan Arena"
        filepath = "C:\\Program Files (x86)\\Thetan Arena\\Thetan Arena.exe"
       
        self.p = subprocess.Popen([filepath,progname])
        
    
    def _end_game(self):
        """
        This is the code for end game
    """
        self.p.terminate()
    
    def _reset_game(self):
        pass
