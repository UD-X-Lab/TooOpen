# DNS query dataset overview

| timestamp    | source IP (anonymized) | source port | domain/URL/name    | class | type | BIND9 label | resolver IP |resolver port	|	Ans	|Dvs|Str| Fth |Label (bot/not) |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 00:00:00.506 | a.a.a.a | 4680 | cookie.pirate | IN | A | +T | v4 | 53 | 8 | 2 | 394 | 187 | bot |
| 00:00:00.654 | z::z | 35314 | graph.facebook.com | IN | A | +E(0)TD | v6 | 853 | 2 | 514 | 27 | 57 | notbot |

The values, `Ans`, `Dvs`, `Str`, `Fth`, refer to Section IV-B of the paper.

The source IPs are anonymized by cryptopANT-1.3.2 (https://ant.isi.edu/software/cryptopANT/index.html ). 

> (2) CryptopANT preserves the classful bits in IPv4 (class A addresses still start with 0/2, class B with 64/3, class C with 128/4, and class D with 196/5)

The query logs on and before June 30, 2025, are labeled. We have also been continuously collecting query logs after June 30, 2025, but without labeling. We can also send these unlabeled datasets after June 30, 2025 to you.


# How to request the DNS query dataset

For privacy concerns, the dataset, with source IPs anonymized, can only be used for research purposes. To request the dataset of DNS query logs, please send the following information using your work or organization/affiliation email address to the first author of the paper by email.

- The approved or waived letter by the Institutional Review Board (IRB) of your institute
- The proposal or the application form that you submitted to the IRB of your institute. In the proposal or application form submitted to the IRB of your institute, you must state that the original data access is limited within the research group members only and shall not be disclosed to any other persons or entities.
- The name(s) and affiliation(s) of you and/or the PI of your research project




# Citation

```latex
@inproceedings{yang2026tooopen,
  title={Too Open to be Secure: An Evaluation of OpenNIC DNS Services and Domains},
  author={Yang, Dianshi and Liang, Xiaoqin and Liu, Daiping and Liu, Guannan and Hao, Shuai and Gao, Xing},
  booktitle={2026 56th Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN)},
  year={2026}
}
```



# List of malicious domains

Folder [bazar](/bazar): BazarBackdoor. (ref: https://malpedia.caad.fkie.fraunhofer.de/details/win.bazarbackdoor)

Folder [bit](/bit): 

- PyXie ([bit/PyXie.txt](/bit/PyXie.txt)): ref: https://web.archive.org/web/20260108114351/https://blogs.blackberry.com/en/2019/12/meet-pyxie-a-nefarious-new-python-rat , https://www.hhs.gov/sites/default/files/pyxie-remote-access-trojan-rat.pdf 
- CoreBot Banking Trojan ([/bit/CoreBot Banking Trojan.txt](/bit/CoreBot%20Banking%20Trojan.txt)): ref: https://web.archive.org/web/20230402064248/https://malwarebreakdown.wordpress.com/2017/09/11/re-details-malspam-downloads-corebot-banking-trojan/ 

Folder [malicious_domains_opennic](/malicious_domains_opennic): malicious domains using OpenNIC TLDs

- [malicious 1.txt](/malicious_domains_opennic/malicious%201.txt) and [malicious 2.txt](/malicious_domains_opennic/malicious%202.txt): malicious domains using OpenNIC TLDs
- [malicious txt.txt](/malicious_domains_opennic/malicious%20txt.txt): malicious domains using OpenNIC TLDs, which specifically use TXT records for botnet C2 or message spreading. The summary of the TXT records is in [TXT record counts 20250618.xlsx](/malicious_domains_opennic/TXT%20record%20counts%2020250618.xlsx).
- Folder [malicious_domains_opennic/groups](/malicious_domains_opennic/groups): categorized of malicious domains using OpenNIC TLDs for botnets, and domains with gTLDs that are related to them.
- Folder [malicious_domains_opennic/groups/casablanca website](/malicious_domains_opennic/groups/casablanca%20website): examples of fake website templates for domains of [malicious_domains_opennic/groups/casablanca.txt](/malicious_domains_opennic/groups/casablanca.txt). According to https://www.virustotal.com/gui/file/57b77ee876cada6c91c4ea3c2ee40b2475c8ffce5d563f860d8c7c24ddbac847/behavior , `casablanca.dyn` and `starship.gopher` may be used for Hailbot botnet C2.

| Category                         | Reference                                                    |
| -------------------------------- | ------------------------------------------------------------ |
| Gafgyt (unclassified 4ea70f)     | https://www.virustotal.com/gui/file/6bcf34bc00dfc49bbc6454b02012c9faf8a1fee28e2b02cceec40cc05bd3b67c/detection |
| CatDDoS                          | https://blog.xlab.qianxin.com/catddos-derivative-en/<br />https://www.secrss.com/articles/75610<br />https://urlhaus.abuse.ch/host/banthis.su |
| Gafgyt (xaiverbot.net)<br />Serisbot | https://www.virustotal.com/gui/file/0f9c2f045570a00291bb9e6442ebd3afd08e75ef167ae6bba9695e401c68147b/behavior<br />https://ducklingstudio.blog.fc2.com/blog-entry-416.html<br />https://x.com/TuringAlex/status/1881217211836273019 <br />https://ti.qianxin.com/case/detail?community=0&id=2580 (need QAX TI account for login) <br />https://ti.qianxin.com/case/detail?community=0&id=2596 (need QAX TI account for login) <br />https://x.com/Xlab_qax/status/1983832927378272441 |
| Hailbot                          | https://threatfox.abuse.ch/ioc/1402169<br />a9e82f0f966c8d2dd293a6b3a93b5cdd2a57a39e1a72c36f904f42c4b67574c7<br />00f4e2d89b586a4ae4c59fd2a08ffe632cdea8193fb1327881a84f72c1deef64<br />4ee026d9455d2d82932054d36c2ea3c38afa92a1bf28bd8e33c7b8ac6289741a<br />409b1e8b9e707deb5874f6b91454e8d31377bf324fc1ade2b1f74b622db4387a<br />https://www.antiy.net/p/20250205-analysis-of-botnet-samples-related-to-attacks-on-deepseek/<br /> |
| Pupy                             | 65ad98ce404068e874c6a45d08f2a70b<br />https://malpedia.caad.fkie.fraunhofer.de/details/win.pupy |
| RapperBot                        | https://blog.xlab.qianxin.com/rapperbot-en/<br />2bd29e874ce83e7ce7b4ea0bbeecb8af77988b00e3c67fb9a41967617180c746<br />https://www.antiy.net/p/20250205-analysis-of-botnet-samples-related-to-attacks-on-deepseek/ |
| Rhadamanthys                     | https://malpedia.caad.fkie.fraunhofer.de/details/win.rhadamanthys<br />https://www.europol.europa.eu/media-press/newsroom/news/end-of-game-for-cybercrime-infrastructure-1025-servers-taken-down<br />https://ti.qianxin.com/case/detail?community=0&id=2579 (need QAX TI account for login)<br />https://ti.qianxin.com/v2/search?type=ip&value=45.153.34.242 (need QAX TI account for login) |
| Gafgyt bashdlod                  | ef262d345309f25040aa78b6317fee5f0ea408ed28f7800b94f068a289cf33fa<br />2d71275cbf7f79207f02c32cf0e70790e8a1bc9db13660816bdcc3631ea8753e<br />843bade6d9057a37b53cd8747a5775bdf62c35e5e03cc62686568d41f2e7be27<br /> |
| Mirai SAgnt / marsilia Apost     | 770a224748c59cad28b9078315a0c8236c1b85e5bb76f868c44139911137775f<br />afba172ae36cc92807974548787c6e6318e5e47dd76317122481180d4ad27196<br />efd2a9e9a88c25c629a9c6cb57b70bd98b9a9fc1c0c791dd870fb6f72dd944d0<br />7e6805617736ed0fb4133c9c787363a51bd572226b119a16629e7c37f9708e39 |
| Mirai (unclassified group6)      | 095221579c748ae9412e4c8b146998009bead5f3d5379c93a6cb95468ce46dad<br />019907c9e0b974dcd26acc9fcc26b954ef77f09672e7b04891d261d0842a583e<br />https://www.joesandbox.com/analysis/1631664/0/pdf<br />https://www.joesandbox.com/analysis/1662040/0/pdfexecutive<br />https://www.joesandbox.com/analysis/1664962/0/pdf |
| keepbanningme                        | https://ti.qianxin.com/case/detail?community=0&id=2816 (need QAX TI account for login)<br />3eea1386a5ffe08e1f7aa442b32d3ab7<br />026fa539bdc6ecbf12200e1f3bb1c125<br />5d5b4f5e54fa7bc35f37e04a8224471c<br />7e76518e49a7b0a3c98058d27227e7dd<br />7a215483239fe9e5eda6446c75cce43b |



