#encoding:gbk
from src.ui import UI
import sys
import  curses

class Menu(object):
    def __init__(self):
        print(sys.getdefaultencoding())
        if sys.getdefaultencoding().upper() == 'ASCII':
            reload(sys);
            sys.setdefaultencoding('gbk')
        self.dataType = 'main'
        self.title = '网易云音乐'
        self.dataList = ['排行榜','艺术家','新碟上架','精选歌单','我的歌单','DJ节目','打碟','收藏','搜索','帮助'];
        self.offset = 0
        self.index = 0;
        self.step = 10;
        self.ui = UI();

    def start(self):
        #构建主菜单
        self.ui.buildMenu(self.dataType,self.title,self.dataList,self.offset,self.index,self.step)
        while True:
            ch = self.ui.screen.getch()
            with open('F:\\keyValues.txt',"a") as fin:
                fin.write(str(ch)+'\n');
            if curses.KEY_UP == ch:
                pass
            elif curses.KEY_DOWN == ch:
                pass



if __name__ == '__main__':
    Menu();