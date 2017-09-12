#encoding:gbk
import curses;
import locale
locale.setlocale(locale.LC_ALL,'')
code = locale.getpreferredencoding();
class UI(object):
    def __init__(self):
        self.screen = curses.initscr();
        curses.cbreak();
        self.screen.keypad(1);
        #��ʼ��8����ɫ
        curses.start_color();
        #��ʼ����ɫ��
        curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK);
        curses.init_pair(2,curses.COLOR_CYAN,curses.COLOR_BLACK);
        curses.init_pair(3,curses.COLOR_RED,curses.COLOR_BLACK);
        curses.init_pair(4,curses.COLOR_YELLOW,curses.COLOR_BLACK);
    def buildMenu(self ,dataType, title, dataList, offset, index, step):
        #�ƶ��������е�һ��
        self.screen.move(4,1);
        #������ǰ��굽EOF�������
        self.screen.clrtobot();
        #���Ʊ��⵽4��19�д�
        self.screen.addstr(4,19,title,curses.color_pair(1));

        if dataType == 'main':
            for i in range(len(dataList)):
                if i == index:
                    self.screen.addstr(i + 8, 16, '-> '+str(i)+'. '+dataList[i],curses.color_pair(2))
                else:
                    self.screen.addstr(i + 8, 19, str(i)+'. '+dataList[i]);
        else:
            pass
        #ˢ�²���ʾ
        self.screen.refresh();












if __name__ == '__main__':
    UI().buildMenu()