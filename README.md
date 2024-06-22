# Psy-Insight
Psy-Insight: Mental Health Oriented Interpretable Multi-turn Bilingual Counseling Dataset for Large Language Model Finetuning
## Examples
While updating the anonymized repository, we encountered a problem; we attempted to integrate a dynamic chat interface into the static website.

### Chinese Examples
### English Examples
```json
{
        "theme": "solution-focused brief therapy: addressing school attendance and academic challenges in students.",
        "is_same_qa": 0,
        "is_same_case": 1,
        "background": "A student struggling with attendance and academic performance",
        "pre_reasoning": "The student has been facing challenges with school attendance and academic performance, as discussed in the previous session.",
        "topic_dialog": {
            "key": "fewshot",
            "unit_id": 97,
            "method": "Solution-Focused Brief Therapy",
            "dialog": [
                {
                    "id": "97-0",
                    "participant": "Therapist",
                    "text": "Yes, you’ve been able to get to school sometimes but not as much as you may want. I’m impressed, though, with how you are at least trying to make it to school these last few weeks since we talked. There must be a lot going on that makes it harder for you to come to school as much as you would like. I’m curious; is there anything that would be helpful to talk about that might help even a little bit?",
                    "reasoning": "Therapist acknowledges the student's efforts and explores potential topics for discussion to offer support.",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "id": "97-1",
                    "participant": "Beth",
                    "text": "Maybe … I don’t know if I can … not sure …it is very hard and I don’t know what will happen if I talk about it.",
                    "observation": "Beth expresses uncertainty and difficulty in opening up.",
                    "emotional label": [
                        "Anxiety",
                        "Fear"
                    ]
                },
                {
                    "id": "97-2",
                    "participant": "Therapist",
                    "text": "Well, in what way do you think it might help if you did share it with me or someone else? Do you think it would make things better for you … like feeling like coming to school?",
                    "reasoning": "Therapist encourages Beth to consider the potential benefits of sharing her concerns.",
                    "strategy": [
                        "Question"
                    ]
                },
                {
                    "id": "97-3",
                    "participant": "Beth",
                    "text": "I don’t know. It might make things even worse.",
                    "observation": "Beth expresses fear that sharing may worsen the situation.",
                    "emotional label": [
                        "Fear"
                    ]
                },
                {
                    "id": "97-4",
                    "participant": "Therapist",
                    "text": "It must be very important to you if it might make things worse. Even though it sounds like if you were to get some help with this issue, it might make your life easier in doing the things you seem to want to do, like school. That is a tough place to be. What would be the most helpful for us to do that might help move you to a better place and feeling better?",
                    "reasoning": "Therapist acknowledges the significance of Beth's concerns and explores ways to support her in improving her situation.",
                    "strategy": [
                        "Question",
                        "Reflection of Feelings"
                    ]
                }
            ]
        },
        "post_reasoning": "The student begins to share her experience, possibly due to feeling accepted and supported by the therapist, indicating a growing trust in the therapeutic relationship."
    }
```


