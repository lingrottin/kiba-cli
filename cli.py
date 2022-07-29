from posixpath import dirname
import sys,os;
from src.libraries.maimai_best_40 import generate as generateBest;
from src.libraries.image import image_to_base64;

os.chdir(dirname(sys.argv[0]));
    

if sys.argv[1] == 'b40' or sys.argv[1] == 'b50':
    if sys.argv[1] == 'b50':
        payload={
            'b50': True,
            sys.argv[2]: sys.argv[3]
        }
    else:
        payload={
            sys.argv[2]: sys.argv[3]
        }
    img,statusCode="",0
    try:
        image, statusCode=generateBest(payload);
    except Exception as e:
        print(f"生成失败（内部错误）：{e}");
    else:
        if(statusCode!=200):
            if(statusCode == 400):
                print("此玩家 ID 没有找到。\n请检查一下您的用户名是否输入正确或有无注册查分器系统。如您没有输入ID，请检查您的QQ是否与查分器绑定正确。\n若需要确认设置，请参阅:\nhttps://www.diving-fish.com/maimaidx/prober/");
            elif(statusCode == 403):
                print(f"查询被禁止\n{sys.argv[3]} 不允许使用此方式查询 Best 40。\n如果是您的账户，请检查您的QQ是否与查分器绑定正确后直接输入“b40”。\n您需要修改查分器设置吗？请参阅:\nhttps://www.diving-fish.com/maimaidx/prober/")
            else:
                print(f"生成失败（服务器错误）：未知状态码{statusCode}，请报告给我的管理员。");
        else:
            print(f"base64://{str(image_to_base64(image), encoding='utf-8')}");
