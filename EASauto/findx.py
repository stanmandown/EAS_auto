import aircv as ac


#imgsrc = ac.imread('taget.png')
#imgobj = ac.imread('pic.png')
def matchImg(imgsrc, imgobj, confidencevalue):  # imgsrc=原始图像，imgobj=待查找的图片
    imgsrc = ac.imread(imgsrc)
    imgobj = ac.imread(imgobj)
    match_result = ac.find_template(imgsrc,imgobj,confidencevalue)  # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    if match_result is not None:
        match_result['shape'] = (imgsrc.shape[1], imgsrc.shape[0])  # 0为高，1为宽
    return match_result