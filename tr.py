import sys
from tkinter import *
from tkinter import ttk
import os
import threading
import subprocess
import queue
from tkinter.scrolledtext import ScrolledText

file_img = """
iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNC
SVQICAgIfAhkiAAAAAlwSFlzAAAAdgAAAHYBTnsmCAAAABl0RVh0
U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAHhSURBVDiN
hVIxaFRREJz376uFRCJqgkUK0UAOcyBYi4KNjSjigYJoOgUbCQEL
SwvBQtD2ahHCVTZ2Ino2QrAI3jUBE1QEJYUguX/v78xa/LvL9weS
B8t7+5id2WUnoHIuP+ucNhs8Fu0szY6JJub225i/y8Ng6dOTO5tl
fFolkMXnbvaaziDyKklIPOjSQsIkAFjYncBtmlJDtBnRIBpIgiRk
1qjik+oHjW1ZLoorFFsiIRpkBtKqcKTN5eVaf2PqKZVfp9mESFCC
U5BxW52EG+E/l9oIfh5u72HJrTT7NnWfssURiOO2i1ulHCE4gh+C
4lEoXoPyuwmNlzQuLu5yTiveALAv0WewPwf2AfYBbV1IKTvFihKZ
9yT9GBE53A/U0H27+KUGZjNQxDBOpiKtrD43/fdR60a3gYDZ4VpG
4NtQPAyOiwHFiVS0NZH1gkSrrZu9M3A04QDcUCn4Pzz2EiPfbI+Q
r8O9XihHgNkewVdpSCZb4q9ZUedkXIPzREVpBcwBDUrKOYDwEd3j
L0PVGP793ioU54dgB2MbHotROPga5j883NWJYOalNgOUNWHZJDTY
QNDFPa0M9TvjPY/3PSBcBnhnh5V3EGzpAWrZOjxegWIdrv0AjsCx
ifDnRRX+Dwgo34LTQaGUAAAAAElFTkSuQmCC
"""
dir_img = """
iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAABGdB
TUEAALGPC/xhBQAAAAlwSFlzAAAScgAAEnIBXmVb4wAAAihJREFU
OE990vtv0kAcAPDh4wd/8w/yp5n4i4kkmizoBMKcRIfG7YepWSSZ
MSTGSXQao8wtjIw5ZkJEJ4+O0CGvoWhSCmw0sFJaHoU+GEJbyDax
EwMjQS+Xy30v97m7791JOF4Y+FMOBEJsj508PXD8lERyoj3Yp4ig
XclNRSlyg0F0TFxLRbXFyAMqaarkQrXabmfO4eqdoBRWtgQnujGM
+DRVbIYnTU3Wvrf7hcubGRToTOsFvK3V/JZyy6KeCXL7CZc3CEVj
k7bTO85/A+FDgwr6rKNIQEtu6XnC0Ch/+j+wCSXXulke994vxh/X
sNkGaaXTfXfYVLbEIwk2gbQBpstxz0QOmq6mdXxxmUr1A8Wg4i8o
rLoWh2C3hvhxr5KcqhMLVMrRJ4eCX97irL/qFh6fdxkvQoAaj4yz
iTv17KsyYu8D8t7hg+q7fXahjr50GaWQawT7OkbDN3/u6JIflQxb
qXN8zzsQniv7tGGv9Czx/tz64gXIqcTCagoaqWxpcO/dKBzL4oTI
uu+QBYaaBX2DeBgyDoJmKQzIMyEVE5Wz8HXMO7W29tnnD8TiiS5A
HbIGPi1kJn3zZzdWLh2CoIKGZHRUlXJPzs29XVoy40SuC6p0lgyo
+PS4e/aM8835GHALDWvY2LVybAxcVs881XtAUEyjC8SEGPx7bfu2
4/mgzfwiEgSz4dcJixRxjq5YVtEM1r6oHiDGuP9RwHS1TOaP/tCj
/d+VL1STn8NNZQAAAABJRU5ErkJggg==
"""


class Application:
    def __init__(self):
        self.app = Tk()

        self.app.title("🌲🏃‍♂️")
        self.app.geometry("800x600")

        # Create the queue
        self.queue = queue.Queue()

        # Create the panes and frames
        self.panedwindow = PanedWindow(self.app, orient=HORIZONTAL)
        self.left_frame = Frame(self.panedwindow)
        self.right_frame = Frame(self.panedwindow)
        self.panedwindow.add(self.left_frame)
        self.panedwindow.add(self.right_frame)
        self.panedwindow.pack(fill=BOTH, expand=1)

        # Create the treeview
        self.treeview = ttk.Treeview(self.left_frame, show='tree')
        self.treeview.pack(fill=BOTH, expand=1)

        # Create the text boxes
        self.input_text = ScrolledText(self.right_frame)
        self.input_text.pack(fill=BOTH, expand=1)
        self.output_text = ScrolledText(self.right_frame)
        self.output_text.pack(fill=BOTH, expand=1)

        self.f = PhotoImage(data=file_img)
        self.d = PhotoImage(data=dir_img)

        start_path = os.path.join(os.path.dirname(__file__), "recipes")
        start_dir_entries = os.listdir(start_path)

        parent_iid = self.treeview.insert(parent='',
                                          index=0,
                                          text='recipes',
                                          open=True,
                                          image=self.d,
                                          tags=("./recipes",))

        # inserting items to the treeview
        self.new_folder(parent_path=start_path,
                        directory_entries=start_dir_entries,
                        parent_iid=parent_iid,
                        f_image=self.f,
                        d_image=self.d)

        # Bind the treeview double click
        self.treeview.bind("<Double-1>", self.on_double_click)

        # Start the queue checking
        self.app.after(100, self.check_queue)

    def new_folder(self, parent_path, directory_entries,
                   parent_iid, f_image, d_image):
        """Creates a graphical representation of the structure
        of subdirectories and files in the specified parent_path.

        Recursive tree building for large directories can take some time.

        :param parent_path: directory path, string
        :param directory_entries: List[str]
               a list containing the names of the entries in the parent_path
               obtained using os.listdir()
        :param parent_iid: unique identifier for a treeview item, string
        :param f_image: file icon, tkinter.PhotoImage
        :param d_image: directory icon, tkinter.PhotoImage
        :return: None
        """
        for name in directory_entries:
            item_path = parent_path + os.sep + name
            # optional: file does not exist or broken symbolic link
            # if not os.path.exists(item_path):
            # print("Skipped:", item_path)
            # continue
            if os.path.isdir(item_path):
                # set subdirectory node
                subdir_iid = self.treeview.insert(parent=parent_iid,
                                                  index='end',
                                                  text=name,
                                                  image=d_image,
                                                  tags=(item_path,))
                try:
                    # pass the iid of the subdirectory as parent iid
                    # all files/folders found in this subdirectory
                    # will be attached to this subdirectory node
                    subdir_entries = os.listdir(item_path)
                    self.new_folder(parent_path=item_path,
                                    directory_entries=subdir_entries,
                                    parent_iid=subdir_iid,
                                    f_image=f_image,
                                    d_image=d_image)
                except PermissionError:
                    pass
            else:
                self.treeview.insert(parent=parent_iid,
                                     index='end',
                                     text=name,
                                     image=f_image,
                                     tags=(item_path,))

    def on_double_click(self, event):
        item_id = self.treeview.selection()[0]
        script_path = self.treeview.item(item_id, "tags")[0]
        if not script_path.endswith(".py"):
            return
        input_text = self.input_text.get("1.0", END).strip()
        threading.Thread(target=self.run_script, args=(script_path, input_text), daemon=True).start()

    def run_script(self, script_path, input_text):
        args = [sys.executable, "-u", script_path]
        process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT, universal_newlines=True, encoding="utf-8")

        output = process.communicate(input=input_text)[0]
        print(output)
        self.queue.put(output)

    def check_queue(self):
        try:
            t = self.queue.get(block=False)
            self.output_text.insert(END, t + "\n")
        except queue.Empty:
            pass
        finally:
            self.app.after(100, self.check_queue)


if __name__ == "__main__":
    app = Application()
    app.app.mainloop()
