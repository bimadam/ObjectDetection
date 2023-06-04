# Object detection in images

## How to run
1) Install dependencies.

```bash
pip install cython pillow>=7.0.0 numpy>=1.18.1 opencv-python>=4.1.2 torch>=1.9.0 --extra-index-url https://download.pytorch.org/whl/cpu torchvision>=0.10.0 --extra-index-url https://download.pytorch.org/whl/cpu pytest==7.1.3 tqdm==4.64.1 scipy>=1.7.3 matplotlib>=3.4.3 mock==4.0.3
```


2) Install **ImageAI** library.

```bash
pip install imageai --upgrade
```

2) Install **PyTorch** library.

```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
```

3) Download **Tiny Yolo V3** model from [here](https://drive.google.com/file/d/1WdOF4NGx1JKzLhLetLMppvokwiYSIa9s/view?usp=sharing).

4. Create folder and put **recognition.py** and **tiny-yolov3.pt** in it.
5. Create two folders: **Input** and **Output**.

This is how your folder should look. (**newimage.jpg** is created after running a code)

![folders](https://i.imgur.com/cToX3wN.png)

## Usage

1. Put any image in **Input** folder. Please note that image has to be **.jpg**.
2. Just run **recognition.py**. Your output should look like this:

![output](https://i.imgur.com/A9jqLgq.png)
3. After running **recognition.py** was created **newimage.jpg** in **Output** folder where you can see detected objects.

![image](https://i.imgur.com/rmNkpNu.jpg)
