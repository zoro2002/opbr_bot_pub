from time import sleep
import win32gui, win32ui, win32con, win32api

def main():
    window_name = "BlueStacks"
    hwnd = win32gui.FindWindow(None, window_name)

    win32gui.SetForegroundWindow(hwnd)
    # win.PostMessage(window_name, win32con.WM_KEYDOWN, 0x43)

    win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x43, 0)
    sleep(0.5)
    win32gui.SendMessage(hwnd, win32con.WM_KEYUP, 0x43, 0)

    # win.SendMessage(win32con.WM_CHAR, ord('c'), 0)
   

def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd),"'" + win32gui.GetWindowText(hwnd) + "'")
    win32gui.EnumWindows(winEnumHandler, None)

def list_inner_windows(whndl):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True
    hwnds = {}
    win32gui.EnumChildWindows(whndl, callback, hwnds)
    print(hwnds)

main()