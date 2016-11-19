# ESLPod 音频下载器

ESLPod 在 iOS 的播客里面总是下载不了，于是做了这个工具用来自动
从 ESLPod 官网同步最新的音频文件到本地。

## Install

    pip install https://github.com/graycarl/ESLGet/archive/master.zip

## Usage

首选选择一个目录用来存放下载下来的音频文件，建议使用默认位置

    ~/Music/eslpods

然后直接运行 `esldl` 命令，并制定音频文件位置：

    esl-get --path ~/SomePlace/here

esldl 会自动找到本地没有的新音频并下载下来：

```
# esl-get --path ~/SomePlace/here
Html load ok.
9 items found.
[ESL Podcast 1261 – Reading About Research on Health.mp3] is already exists, ignore.
[English Café 581.mp3] is already exists, ignore.
Start to download [ESL Podcast 1260 – Transport and Shipping Mishaps.mp3]
Downloading  [####################################]  100%
[ESL Podcast 1259 – Discovering a Family Secret.mp3] is already exists, ignore.
[English Café 580.mp3] is already exists, ignore.
[ESL Podcast 1258 – Causes of Plane Crashes.mp3] is already exists, ignore.
[ESL Podcast 1257 – Repairing Damage to an Auto Body.mp3] is already exists, ignore.
[English Café 579.mp3] is already exists, ignore.
[ESL Podcast 1256 – Describing Fast and Slow Speech.mp3] is already exists, ignore.
[ESL Podcast 1255 – Talking About Gemstones.mp3] is already exists, ignore.
Done.
```
