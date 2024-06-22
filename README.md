# Psy-Insight
Psy-Insight: Mental Health Oriented Interpretable Multi-turn Bilingual Counseling Dataset for Large Language Model Finetuning
## Examples
we attempted to integrate a dynamic chat interface into the static website.While updating the anonymized repository, we encountered a problem.

### Chinese Examples
```json
{
        "theme": "",
        "chat_stage": "4th Session",
        "is_same_qa": 1,
        "is_same_case": 1,
        "background": "来访者是一位经历过情绪创伤的个体，敏感且对特定词语或触发事件有情绪反应。她可能正在通过心理咨询寻找情绪释放和自我成长，同时展示了治疗的进展和信任关系的建立。",
        "pre_reasoning": "治疗师发现自已无意间用了“猜”这个词，就是这个词在上次咨询时触发了来访者的情绪爆发，而这个词无疑也和她当初的伤痛有关。在即将说出这个词的那一刻，治疗师心里曾闪过一丝犹豫，不过他没换词，这样做的第一个原因是：人不可能长时间刻意控制自己，不管怎样，每个人都有自己的言语习惯，如果治疗师和张三说话时必须避开这个词，和李四说话又要避开那个词，那么他的注意力就会被转移开，无法专注于来访者述说的内容。第二个原因：在某种程度上，治疗师必然是感受到了，来访者现在有能力参与治疗了，使用“猜”这个词，也在传达治疗师的信心，治疗师相信来访者有能力更有效地处理先前使她伤心难过的事情。\n",
        "topic_dialog": {
            "key": "fewshot",
            "unit_id": 148,
            "method": "Unknown",
            "dialog": [
                {
                    "text": "是的，他开始接受心理治疗训练时，我是他最初几个来访者之一。三年后，他完成了培训，决定自己开诊所了。",
                    "participant": "来访者",
                    "id": "148-0",
                    "emotional label": [
                        "Neutral"
                    ]
                },
                {
                    "text": "在他离开之前，你们讨论过他的离开在你心理上，以及现实层面上的影响么？",
                    "participant": "治疗师",
                    "id": "148-1",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "labels": [
                        {
                            "label": "（停住）",
                            "index": 47,
                            "type": "dialogue_act"
                        }
                    ],
                    "text": "（停住）哦，这个讨论过。他在离开前大约六个月便告诉我了，在他确定知道自己接下去要做什么时，就立即说了。",
                    "participant": "来访者",
                    "id": "148-2",
                    "emotional label": [
                        "Neutral"
                    ]
                },
                {
                    "text": "嗯？",
                    "participant": "治疗师",
                    "id": "148-3",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "text": "我和他都知道，我可能还没完成关于我对父亲感觉的分析。毫无疑问，治疗应该继续下去，或许还要好几年时间，可是治疗费用成了问题。",
                    "participant": "来访者",
                    "id": "148-4",
                    "emotional label": [
                        "Anxiety",
                        "Unknown"
                    ]
                },
                {
                    "text": "费用怎么了？",
                    "participant": "治疗师",
                    "id": "148-5",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "text": "嗯，我那时只是个大学生啊，就跟现在一样，我不可能付得起看私人诊所的费用。",
                    "participant": "来访者",
                    "id": "148-6",
                    "emotional label": [
                        "Anxiety",
                        "Unknown"
                    ]
                },
                {
                    "text": "那么，然后怎样了？",
                    "participant": "治疗师",
                    "id": "148-7",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "text": "就这个问题我们争了起来，他让我向父亲索取治疗费，而我不愿意。",
                    "participant": "来访者",
                    "id": "148-8",
                    "emotional label": [
                        "Anger"
                    ]
                },
                {
                    "text": "你的意思是，你觉得你父亲负担不起么？",
                    "participant": "治疗师",
                    "id": "148-9",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "text": "哦，不是这个意思，我父亲是个医生，经济上很宽裕，只是我不想为这件事去找他。",
                    "participant": "来访者",
                    "id": "148-10",
                    "emotional label": [
                        "Others"
                    ]
                },
                {
                    "text": "为什么呢？",
                    "participant": "治疗师",
                    "id": "148-11",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "text": "陪，爸爸不相信心理治疗。直到今天，我也没告诉过他我在接受心理治疗。",
                    "participant": "来访者",
                    "id": "148-12",
                    "emotional label": [
                        "Fear"
                    ]
                },
                {
                    "text": "而李医生觉得你应该告诉他？",
                    "participant": "治疗师",
                    "id": "148-13",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "text": "不，不是，事实上我都没跟李医生说过我父亲的这个态度。我觉得没那必要。我的想法是，李医生应该按原先的价格收我的治疗费，毕竞，他利用我完成他的训练，还从来没回报过我呢。",
                    "participant": "来访者",
                    "id": "148-14",
                    "emotional label": [
                        "Anger"
                    ]
                },
                {
                    "text": "你跟他说过这些想法么？",
                    "participant": "治疗师",
                    "id": "148-15",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "text": "是啊，然后他就生我气了，气得不行。我记不得他当时具体都说了什么，不过在那之后变化挺大的。之前他一直是个挺温和的人，后来他就发火的事儿也向我道了歉，我们接下去又谈了几个月，但是，感觉就是不一样了。再然后，我决定要停止治疗，尽管他认为我应该继续，至少在他离开医院之前继续治疗；我也知道自己需要继续治疗，可是，或许我那会儿已经感受不到对他的信任了，我不相信他能够理解我，我猜。",
                    "participant": "来访者",
                    "id": "148-16",
                    "emotional label": [
                        "Sadness"
                    ]
                },
                {
                    "text": "在我听来似乎是这样：你预想自己不得不告诉父亲你正在接受心理治疗，而且还要请求他资助，然后就被吓着了但是你没有将这些恐惧当做治疗的一部分，和李医生详加讨论，而是用激怒他的方式把这个部分掩藏起来了，并且视他的恼怒为你退出治疗的一个理由。这样一来，你就无需让父亲知道你需要钱做治疗了。本质上，你是栖牲掉了自已的治疗，并承受着损失治疗所带来的痛苦，而这样做，是为了能规避一些东西，那些你似乎觉得会带给你更大伤害的东西。",
                    "participant": "治疗师",
                    "id": "148-17",
                    "strategy": [
                        "Reflection of Feelings"
                    ]
                },
                {
                    "text": "治疗对我意义那么大，我都被迫放弃治疗了，还能有什么比这个更伤害我？",
                    "participant": "来访者",
                    "id": "148-18",
                    "emotional label": [
                        "Depression"
                    ]
                },
                {
                    "text": "在你考虑到要去告诉父亲你在接受心理治疗，还要跟他要钱支付费用时，你会想到什么？来：我爸脾气很可怕，只要惹到他了，根本就没法预料他会做什么。我确定，要是他知道我来见你，肯定会大发牌气。在我们第一次碰面时，我的印象是，你跟父亲很亲密一一他真会对你大发脾气么？",
                    "participant": "治疗师",
                    "id": "148-19",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "text": "你不了解我爸，他能一件事儿记恨好久。我弟弟Henry，小我3岁，生下来就弱智，这件事他一直都在怪我妈妈，认为都是她的错，怪我妈的家族有精神病史。",
                    "participant": "来访者",
                    "id": "148-21",
                    "emotional label": [
                        "Anger"
                    ]
                },
                {
                    "text": "即便是基因遗传；也没法说是妈妈有错呀？",
                    "participant": "治疗师",
                    "id": "148-22",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "text": "还不止这样呢。我爸一发现Henry是先天愚型，就立刻要把他送到收容所去；而我妈无法接受这么做。于是所有人、所有事，她都不管不顾了，只把全副身心都扑在这孩子身上。尽管如此，在Henry长到10岁左右时，妈妈最终还是意识到，她再也无力在家里应付这孩子了，我们最终还是不得不把他送走。",
                    "participant": "来访者",
                    "id": "148-23",
                    "emotional label": [
                        "Sadness"
                    ]
                },
                {
                    "text": "这整件事，你怎么想？",
                    "participant": "治疗师",
                    "id": "148-24",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "text": "我没想过，或者说，我是试图不去想。或许早一点面对现实会好些吧，可是对一个母亲来说，这么做太难了。",
                    "participant": "来访者",
                    "id": "148-25",
                    "emotional label": [
                        "Sadness"
                    ]
                },
                {
                    "text": "尤其是，假如在这件事上她觉得自己有过失的话，就会更加难做。",
                    "participant": "治疗师",
                    "id": "148-26",
                    "strategy": [
                        "Reflection of Feelings"
                    ]
                },
                {
                    "text": "我同意。外限来访者开始积极讲述上次曾引发她强烈情绪的那些事，这是个很好的预后征兆。她自发地描述其个人生活里的重要事件，这表明了治疗在向前推进。",
                    "participant": "来访者",
                    "id": "148-27",
                    "emotional label": [
                        "Unknown"
                    ]
                }
            ]
        },
        "post_reasoning": "在治疗情境中，治疗师的策略包括逐步熟悉来访者、处理来访者的移情关系以及审慎地调节来访者的过度反应。治疗师不仅创设包容的氛围，还帮助来访者面对自己对治疗师的态度，并揭示、检视她的困难。治疗师不轻易附和来访者的态度，也不忍受来访者的无礼行为，除非这些行为能促进对来访者性格和问题的深入理解。在来访者的案例中，治疗师的策略使得来访者逐渐接受治疗，不再试图讨价还价，而是默默接受了治疗师的帮助。治疗师的策略旨在建立积极的治疗关系，促进来访者的自我认知和改变。",
        "extra_tags": [],
        "guide": "治疗师的信任和支持对她的情绪整合和疗愈过程至关重要。"
    },
```
### English Examples
```json
{
        "theme": "solution-focused brief therapy: building trust in the therapeutic relationship through acceptance and support for students sharing their experiences.",
        "is_same_qa": 0,
        "is_same_case": 0,
        "background": "A student confides in the therapist about a disturbing experience with her uncle and her concerns about her mother's reaction.",
        "pre_reasoning": "The student's willingness to share her experience may indicate that the therapist's acceptance and support have built trust in the therapeutic relationship.",
        "topic_dialog": {
            "key": "fewshot",
            "unit_id": 98,
            "method": "Solution-Focused Brief Therapy",
            "dialog": [
                {
                    "id": "98-0",
                    "participant": "Beth",
                    "text": "It’s my older uncle … He comes over a lot and stays with us, and sometimes my mom leaves us with him when she goes out. I liked him, but last semester he stayed over and he wanted to kiss me. I didn’t know what to do. My mom likes him a lot, and they are close. Now, he says he loves me, and he has put his hands on me, you know, my breasts. I just stood there and didn’t know what to do. I don’t want to let mom know; she would be mad at me.",
                    "observation": "Beth discloses a distressing experience involving her uncle, expressing confusion and fear about the situation and concern about her mother's reaction, indicating a complex family dynamic and her reluctance to cause conflict.",
                    "emotional label": [
                        "Fear",
                        "Shame"
                    ]
                },
                {
                    "id": "98-1",
                    "participant": "Therapist",
                    "text": "Thank you for taking the chance and trying to help your situation by sharing it with me. I understand how difficult it must have been for you keeping this secret and trying to protect your mom’s relationship with her brother. I admire your courage to take care of yourself given the very difficult situation you’ve been in. Do you have any ideas about how you would want to make this better and not have this happening?",
                    "reasoning": "The therapist acknowledges Beth's bravery in sharing her experience and offers support while encouraging her to consider ways to improve her situation, empowering her to take control and explore solutions.",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "id": "98-2",
                    "participant": "Beth",
                    "text": "I’m aware of child protective services. They see some of my friends and their families. I don’t want to have to leave my mom, and I don’t want her to be mad at me.",
                    "observation": "Beth demonstrates awareness of potential support services but expresses concerns about the impact on her family dynamics, highlighting her internal conflict and the importance of maintaining her relationship with her mother.",
                    "emotional label": [
                        "Fear",
                        "Guilty"
                    ]
                },
                {
                    "id": "98-3",
                    "participant": "Therapist",
                    "text": "I agree that you should be able to stay in your home and also to have a good relationship with your mom. You are aware of child protective services. It is their job to help protect you and any other young person. I agree with you that it is best when you stay at home and make it a safe place for you and your brothers and sisters and your mom, too. From what you have shared, it would be important to contact child protective services. I know several people there, and I would like for you to help me make this contact so that you can make your home safe. Will you help make that happen?",
                    "reasoning": "The therapist validates Beth's desire to maintain her family relationships while emphasizing the importance of her safety, suggesting a collaborative approach to involve child protective services and ensure a safe environment for Beth and her family.",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "id": "98-4",
                    "participant": "Beth",
                    "text": "I guess … But I’m still afraid of what mom might say and of her brother.",
                    "observation": "Beth expresses fear of potential repercussions within her family, indicating the internal struggle she faces in balancing her safety with her relationships and the challenging decisions ahead.",
                    "emotional label": [
                        "Anxiety",
                        "Fear"
                    ]
                },
                {
                    "id": "98-5",
                    "participant": "Therapist",
                    "text": "I understand your not wanting to upset your mom or even your uncle. It’s not an easy decision to make. What do you think would be the best way to handle this so that you don’t have to deal with your uncle’s behavior and you can feel safe?",
                    "reasoning": "The therapist acknowledges Beth's concerns and explores her thoughts on managing the situation delicately, encouraging her to consider strategies that prioritize her safety and well-being while navigating the complexities of family dynamics.",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "id": "98-6",
                    "participant": "Beth",
                    "text": "Do you think the service worker would help me tell my mother and help make things easier after she finds out?",
                    "observation": "Beth's question reflects her uncertainty and concern about how to handle the situation with her mother, indicating a need for support and guidance.",
                    "emotional label": [
                        "Fear"
                    ]
                },
                {
                    "id": "98-7",
                    "participant": "Therapist",
                    "text": "I can only say that that is exactly the work they do with families in these situations. It’s important that you are safe and that your family can continue to be close. And it’s important that the worker understand what happened and then has your help in finding the best way to work with your mom. You can meet and talk with the worker here at school and help her understand the situation. Is that okay with you?",
                    "reasoning": "The therapist acknowledges Beth's concerns and offers reassurance by explaining the role of the service worker and emphasizing the importance of safety and family relationships. By involving Beth in the process and seeking her consent, the therapist empowers her to take an active role in seeking help and support.",
                    "strategy": [
                        "Question"
                    ]
                }
            ]
        },
        "post_reasoning": "The therapist reassures the student about involving child protective services and emphasizes the importance of ensuring her safety and maintaining family relationships. The therapist encourages the student to participate in the process of seeking help and support."
}
```


