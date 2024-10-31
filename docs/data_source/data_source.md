## Data Source \ Copyright of Raw Counseling Data

### Raw Datasets

* **MNBVC dataset**
	* MNBVC: Massive Never-ending BT Vast Chinese corpus

* **Book3** dataset
	* The Pile: An 800GB Dataset of Diverse Text for Language Modeling 

* Crawled Data Source
	* **psyarxiv**  
	* [Emotional First Aid Raw Dataset](https://github.com/chatopera/efaqa-corpus-raw)




#### Personal and Sensitive Information 

The dataset may contain sensitive information related to mental health. All questions and answers have been anonymized to remove any PII data.

#### Dataset For Source Datasets

##### Book3 Dataset

Book3 dataset is Shawn Presser's work and is part of EleutherAi/The Pile dataset. This dataset contains all of bibliotik in plain .txt form, aka 197,000 books processed in exactly the same way as did for bookcorpusopen (a.k.a. books1). seems to be similar to OpenAI's mysterious "books2" dataset referenced in their papers. It comprises an extensive collection of digitized books, spanning from classics to contemporary works. We filter psychotherapy books from Book3 dataset. Include 5000+ turn of counseling conversation. Licensing Information of book3 dataset is MIT license. The *MIT license* gives express permission for users to reuse code for research purpose. Our English counseling part of dataset inherits its MIT copyright license. 

* **Dataset:** [defunct-datasets/the_pile_books3 · Datasets at Hugging Face](https://huggingface.co/datasets/defunct-datasets/the_pile_books3) 
* **Blog:**<img src="https://ckqqqq-qiker-image-service.oss-cn-beijing.aliyuncs.com/typora-image/image-20241031104009954.png" alt="image-20241031104009954" style="zoom:50%;" />
* **MIT license:** [The MIT License – Open Source Initiative](https://opensource.org/license/mit)
* **Bibtex:**

```
@article{pile,
    title={The {P}ile: An 800GB Dataset of Diverse Text for Language Modeling},
    author={Gao, Leo and Biderman, Stella and Black, Sid and Golding, Laurence and Hoppe, Travis and Foster, Charles and Phang, Jason and He, Horace and Thite, Anish and Nabeshima, Noa and Presser, Shawn and Leahy, Connor},
    journal={arXiv preprint arXiv:2101.00027},
    year={2020}
}
```

#### Dataset Card for MNBVC

The MNBVC Open Source Chinese Corpus Project provides a platform for researchers to jointly build and share resources. The goal of MNBVC is to protect the assets of Chinese Internet corpora through the construction of this corpus project and to provide the most basic and universal corpus materials for the development of Chinese AI. Thanks to the [Liwu community](http://mnbvc.253874.net/) for constructing this dataset

* **MIT license:** [MNBVC/LICENSE at main · esbatmop/MNBVC](https://github.com/esbatmop/MNBVC/blob/main/LICENSE)

```
@misc{mnbvc,
  author = {{MOP-LIWU Community} and {MNBVC Team}},
  title = {MNBVC: Massive Never-ending BT Vast Chinese corpus},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/esbatmop/MNBVC}},
}
```

* Preprocess Scripts

	* UTF-8 formatter[charset_mnbvc](https://github.com/alanshi/charset_mnbvc)

	* TXT formatter [deduplication_mnbvc](https://github.com/aplmikex/deduplication_mnbvc)

		

### PsyARXIV

**PsyArXiv** is a [preprint](https://en.wikipedia.org/wiki/Preprint) repository for the psychological sciences. It is hosted by the [Center for Open Science](https://en.wikipedia.org/wiki/Center_for_Open_Science). The preprint service was supported by the [arXiv](https://en.wikipedia.org/wiki/ArXiv) repository. There is the copyright information of Arxiv. [License and copyright - arXiv info](https://info.arxiv.org/help/license/index.html)As a repository for scholarly material, arXiv keeps a permanent record of every article and version posted. All articles on arXiv.org can be viewed and downloaded freely by anyone.

* Website link [ PsyArXiv Preprints](https://osf.io/preprints/psyarxiv)
* Crawler scripts [isLinXu/xxarxiv_mnbvc](https://github.com/isLinXu/xxarxiv_mnbvc)
* License: [License and copyright - arXiv info](https://info.arxiv.org/help/license/index.html)

### [Emotional First Aid Raw Dataset](https://github.com/chatopera/efaqa-corpus-raw)

Emotional First Aid Raw Dataset (EFARD) is a common crawl paid  dataset for psychological dataset. This dataset is composed of data crawled from numerous open data websites, including Yixinli, Douban, etc. We retrieve about 1300 turns of counseling conversations from it. 

* license [cskefu.com/licenses/v1.html](https://www.cskefu.com/licenses/v1.html)
* Crawler scripts: cn_pipeline

