# Psy-Insight
Psy-Insight: Mental Health Oriented Interpretable Multi-turn Bilingual Counseling Dataset for Large Language Model Finetuning
## Examples
we attempted to integrate a dynamic chat interface into the static website.While updating the anonymized repository, we encountered a problem.

### Chinese Examples
```json
    {
        "theme": "",
        "chat_stage": "6th Session",
        "is_same_qa": 0,
        "is_same_case": 1,
        "background": "来访者是一个独居女性，可能对人际关系和自我调适能力有着较强的关注。她可能在与童年记忆和家庭情感联系的治疗中探寻自我认知和解决困难。",
        "pre_reasoning": "治疗师做得很对，不用去等着看来访者会不会跟自已多谈一点室友的事，既然治疗师对此产生了兴趣，就不妨直接问。治疗师选择先问室友的事，而不是问论文，因为了解“室友问题”，或许能使人进一步理解来访者的初始主诉议题：在建立人际关系上遇到困难。\n在“来访者因自己公寓里凌乱而不悦”，与“她的童年记忆，以及当时她母亲抑郁发作后家里的状况”之间，治疗师可能会去尝试建立联系。尽管这之间可能会存在着某种联系，但在本节面询中，尚无证据下这个结论，所以，此刻治疗师没有理由不就其字面意涵来理解来访者。治疗师没有将来访者的思考强行纳入所谓心理动力取向的诠释模式，而是把握这个机会，去了解来访者在面对压力时的反应，了解她调适日常生活的能力。\n",
        "topic_dialog": {
            "key": "fewshot",
            "unit_id": 163,
            "method": "Unknown",
            "dialog": [
                {
                    "text": "我一开始就不该找她合租，但是没办法，我需要个人来分担费用。她年纪比我小很多，而且生活理念也不同。该她分担的家务，她从来都不在乎自己是不是已经完成，也不在乎公寓里乱成什么样。我可不能那样过日子，于是我就跟她说了，结果她还不高兴了。我想她早就在另找房子了吧，现在一定是已经找到了。",
                    "participant": "来访者",
                    "id": "163-0",
                    "emotional label": [
                        "Anger"
                    ]
                },
                {
                    "text": "那现在你打算怎么办呢？",
                    "participant": "治疗师",
                    "id": "164-0",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "text": "在我做论文的研究部门里有个女人，我想她会有兴趣跟我合租。她现在承租的公寓正在卖，无论如何，她过几月也得搬家。",
                    "participant": "来访者",
                    "id": "164-1",
                    "emotional label": [
                        "Neutral"
                    ]
                },
                {
                    "text": "那你怎么知道你们两个合得来呢？",
                    "participant": "治疗师",
                    "id": "164-2",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "text": "我们两个年纪接近，似乎在很多事上的观点也都一致。我们在这个部门相处蛮久了，我想应该不错。",
                    "participant": "来访者",
                    "id": "164-3",
                    "emotional label": [
                        "Neutral"
                    ]
                },
                {
                    "text": "你在这个部门的工作性质是什么？",
                    "participant": "治疗师",
                    "id": "164-4",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "text": "我在参与一个针对领养父母的研究。领养安置之后我做跟进随访，最初，我们对领养父母的亲职能力做过一个评定，现在我要去了解其预估的准确度。",
                    "participant": "来访者",
                    "id": "164-5",
                    "emotional label": [
                        "Neutral"
                    ]
                },
                {
                    "text": "这是你攻读博士学位的一部分么？",
                    "participant": "治疗师",
                    "id": "164-6",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "text": "我打算继续读书，以后拿博士学位，不过现在，我正在完成硕士论文。如果我的导师喜欢我做的研究，那么今年夏天我就能拿到硕士学位了。所以我要好好准备跟他的这次约谈。对了，要是下周我暂停一次和你见面，你会介意么？我要准备见他，时间不够用。",
                    "participant": "来访者",
                    "id": "164-7",
                    "emotional label": [
                        "Anxiety"
                    ]
                },
                {
                    "text": "面询是属于你的，你当然可以取消预约，不过我怀疑取消预约对你不是太好。",
                    "participant": "治疗师",
                    "id": "164-8",
                    "strategy": [
                        "Affirmation and Reassurance"
                    ]
                },
                {
                    "text": "你的意思是，如果我感到太过担心或者烦恼的话，那么，在我和导师见面之前来这里谈谈，会比之后再来要好，是这样么？",
                    "participant": "来访者",
                    "id": "164-9",
                    "emotional label": [
                        "Anxiety"
                    ]
                },
                {
                    "text": "正是。",
                    "participant": "治疗师",
                    "id": "164-10",
                    "strategy": [
                        "Others"
                    ]
                },
                {
                    "text": "我想，下周我还是来吧。对于今天我告诉你的事，你有什么想法么？我想我该道歉，我今天说的尽是些鸡毛蒜皮，都是让人提不起兴趣的事，我的意思是，这些都不是心理层面上的问题。",
                    "participant": "来访者",
                    "id": "164-11",
                    "emotional label": [
                        "Others"
                    ]
                },
                {
                    "text": "我一点都没有觉得无趣啊。看到你有能力应对压力情境，真令人鼓舞，而且了解这些对我来说也是重要的。",
                    "participant": "治疗师",
                    "id": "164-12",
                    "strategy": [
                        "Affirmation and Reassurance"
                    ]
                }
            ]
        },
        "post_reasoning": "在“来访者因自己公寓里凌乱而不悦”，与“她的童年记忆，以及当时她母亲抑郁发作后家里的状况”之间，治疗师可能会去尝试建立联系。尽管这之间可能会存在着某种联系，但在本节面询中，尚无证据下这个结论，所以，此刻治疗师没有理由不就其字面意涵来理解来访者。治疗师没有将来访者的思考强行纳入所谓心理动力取向的诠释模式，而是把握这个机会，去了解来访者在面对压力时的反应，了解她调适日常生活的能力。\n在本次面询中，治疗师采取了多种策略来处理来访者的情绪和行为。首先，治疗师澄清了来访者的焦虑并指出其能力和潜在的成长空间，鼓励她积极参与治疗。治疗师还观察到来访者对自我认知和人际关系的困惑，理解她的需求并给予肯定和指导。此外，治疗师避免了对来访者的负面评价，而是以好奇心和理解回应她的挑战，让来访者感到被接纳和理解。治疗师的策略包括鼓励、肯定、理解和引导，以帮助来访者面对自身问题并获得成长。这些策略有助于建立积极的治疗关系，促进来访者的自我探索和改善。",
        "extra_tags": [],
        "guide": "治疗师的直接问询方式可能为她提供了温暖和支持。"
    }
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


