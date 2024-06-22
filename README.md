# Psy-Insight
Psy-Insight: Mental Health Oriented Interpretable Multi-turn Bilingual Counseling Dataset for Large Language Model Finetuning
## Examples
While updating the anonymized repository, we encountered a problem; we attempted to integrate a dynamic chat interface into the static website.

### Chinese Examples
```json

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


