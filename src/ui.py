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
        #初始化8种颜色
        curses.start_color();
        #初始化颜色对
        curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK);
        curses.init_pair(2,curses.COLOR_CYAN,curses.COLOR_BLACK);
        curses.init_pair(3,curses.COLOR_RED,curses.COLOR_BLACK);
        curses.init_pair(4,curses.COLOR_YELLOW,curses.COLOR_BLACK);
    def buildMenu(self ,dataType, title, dataList, offset, index, step):
        #移动到第四行第一列
        self.screen.move(4,1);
        #擦除当前光标到EOF间的内容
        self.screen.clrtobot();
        #绘制标题到4行19列处
        self.screen.addstr(4,19,title,curses.color_pair(1));

        if dataType == 'main':
            for i in range(len(dataList)):
                if i == index:
                    self.screen.addstr(i + 8, 16, '-> '+str(i)+'. '+dataList[i],curses.color_pair(2))
                else:
                    self.screen.addstr(i + 8, 19, str(i)+'. '+dataList[i]);
        else:
            pass
        #刷新并显示
        self.screen.refresh();












if __name__ == '__main__':
    UI().buildMenu()