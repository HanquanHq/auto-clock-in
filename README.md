## 2022.01.02 Updates

- 11月整月，打卡脚本正常运行，非常爽。

- 12月初，疫情通大升级，连域名都给换了，旧版不能用了，于是回到每日被催打卡的日子。

- 1月元旦期间，我参考 [tsosunchia 同学的脚本](https://github.com/tsosunchia/bjut_autosignin)，更新了 app.py，现在可以正常打卡了。

使用方式是，**抓包拿到你的 id 和 token，放进 app.py 的 userAccounts 里面，然后 `python app.py` 运行即可**。

下面的旧版文档已经过时了，就不用看啦。

## Introduction

A auto clock-in script based on python3 for BJUTer.

It could clock in at 9:00 a.m everyday.

> The script is inspired by [tsosunchia](https://github.com/tsosunchia/bjut_autosignin)

## What can I do ?

- [x] Clock in at 9:00 a.m everyday
- [x] Send the email after clocking in

## Usage

1. Fork the project 

2. Update your information

    - Open `info.json` and complete it with your own information
    
    - The `id` & `token` are easy to get through any network protocol analyzer


      > ⚠️NOTICE
      >
      >  - Once **id & token** are invalid, you have to update the script manually once a week.
      >
      >  - If your mobile device is on iOS, I'm willing to recommend the `Stream` App which is free & concise. For android users, you can install Packet Capture from the Google Play Store :)

3. [option] Email Settings
    > You can escape this step in branch [no-email](https://github.com/galaxyxxxxx/auto-clock-in/tree/no-email)

    Open the settings in your forking repository, add the following info to your secrets.

    ```
    EMAIL_USERNAME 
    EMAIL_PASSWORD 
    EMAIL_SERVER
    EMAIL_PORT
    ```

## Test
Run the script
```shell
python3 app.py
```

## Example

  Inspired by [tsosunchia](https://github.com/tsosunchia/bjut_autosignin)，I extract the user info module as a single file, which is easy for us to update own info.

  A example of `info.json` is listed as below.

  ```json
  {
      "id": "402880c97b5d8ad1017c39dcd10*****",
      "token": "CA6CD39AFDAC284ED68BB81BD54*****",
      "c1": "在籍研究生",
      "c2": "在校内居住",
      "c3": "否",
      "c4": "否",
      "c5": "正常",
      "c6": "正常",
      "c7": "无情况",
      "c8": "在京内",
      "c12": "北京市,北京市,朝阳区,",
      "c9": "否",
      "c10": "否",
      "c11": "否",
      "c14": "未接种",
      "location_longitude": "40",
      "location_latitude": "110",
      "location_address": "这里填写你的地址"
  }
  ```

  ## Thanks
  ✨ [Woodykaixa](https://github.com/Woodykaixa)
