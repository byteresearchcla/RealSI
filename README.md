# RealSI

RealSI: Open Benchmark for Simultaneous Interpretation in Real-world Scenarios

![RealSI](resource/ST.jpeg)

For details of the dataset, please refer to the [Technical Report](https://arxiv.org/abs/2407.21646) of Cross Language Agent-Simultaneous Interpretation, `CLASI`.

## Download

Please follow the instructions to download the dataset.

```bash
pip3 install -r requirements.txt
mkdir data/en2zh/audio data/zh2en/audio

python3 toolkits/download_audio.py
```

## Introduction

`RealSI` is a benchmark for Simultaneous Interpretation(SI) in real-world scenarios. This project intends to release a public test set for SI, in order to evaluate the speech translation performance of the model in difficult scenarios such as long audio, speakers not being fully prepared, and heavy accents.


## Data Construction

Audio data are collected from public videos, covering 2 languages and 10 different topics. We cut out video clips of 3-7 minutes, and label the timestamps, transcripts and translations of speech in the video.

| Domain   | Duration - zh2en | #Segments - zh2en | Duration - en2zh | #Segments - en2zh |
|:---------------|:-----------------:|:--------------:|:-----------------:|:-------------------:|
| Technology | 5:23 | 51 | 3:25 | 31 |
| Healthcare | 3:16 | 30 | 3:34 | 22 |
| Education  | 4:56 | 48 | 5:00 | 41 |
| Finance    | 5:22 | 29 | 5:01 | 40 |
| Law        | 4:38 | 49 | 4:48 | 29 |
| Environment| 4:18 | 34 | 4:24 | 31 |
| Entertainment | 5:16 | 53 | 5:12 | 39|
| Science | 4:47 | 37 | 5:11 | 35 |
| Sports | 5:22 | 33 | 3:25 | 58 |
| Art    | 7:54 | 67 | 4:17 | 21 |
| ***Total*** | ***51:12*** | ***431*** | ***44:17*** | ***347*** |

**DISCLAIMER:** ***We do not own the copyright of the
videos and only release our annotation together with the publicly available website links of the corresponding
videos. If anyone believes that the content constitutes infringement, please contact us. We will remove the
relevant content as soon as possible once confirmed. Any content in this dataset is available for educational and informational purposes only. You are solely responsible for legal liability arising from your improper use of the dataset content. Refer to [License](#lic)***


## Structure Walkthrough

We save each audio in separate files, each file contains information of id and duration of the audio. The utterances are grouped in semantic segments, which convey complete semantic for translation. When conducting human evaluation, we recommend evaluating the model prediction results according to this segmentation.

We show the data structure by taking `en2zh-01-tech` as example.

```json
{
  "vid": "en2zh-01-tech",
  "duration": 205000,
  "segment": [
    {
      "start_time": 0,
      "end_time": 5790,
      "utterance": [
        {
          "sub_start_time": 0,
          "sub_end_time": 2810,
          "sub_src_text": "Round-robin um um load balancing scheme,",
          "sub_trg_text": "轮询负载均衡方案。",
          "term": [
            {
                "src": "Round-robin",
                "trg": "轮询"
            },
            ... ...
          ]
        },
        ... ...
      ],
    },
    ... ...
  ]
}
```


## <a name="lic"></a>License

This dataset is released under the Creative Commons Attribution 4.0 International License. Please refer to [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) for more details.

## Citation
Please cite us as
```
@article{Cheng2024TowardsAH,
  title={Towards Achieving Human Parity on End-to-end Simultaneous Speech Translation via LLM Agent},
  author={Cheng, Shanbo and Huang, Zhichao and Ko, Tom and Li, Hang, and Peng, Ningxin and Xu, Lu, and Zhang, Qini},
  year={2024},
  url={https://arxiv.org/abs/2407.21646}
}
```


