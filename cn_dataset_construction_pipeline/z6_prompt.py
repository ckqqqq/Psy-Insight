input_str=r"""[{"id": "310-0", "participant": "治疗师", "text": "因为上学期在学校里你做得不如你本该做得那么好，所以你不合格，从你所说的，听起来你仍然有一些程度地相信。"}, {"id": "310-1", "participant": "来访者", "text": "是的。\""}, {"id": "310-2", "participant": "治疗师", "text": "我想得到更好一点的理由，你还有什么依据支持你的信念？"}, {"id": "310-3", "participant": "来访者", "text": "可以。\""}, {"id": "310-4", "participant": "治疗师", "text": "我想做的是角色扮演，我扮演你心理上的“理性”部分，即理性地知遵仅仅因为你未能全得A，并不意味着你就是彻头彻尾的不合格，我想让你扮演你心理上的·情绪，部分，你仍然真实地相信你不合格，这是来自于你心里的声音。我想让你尽可能严厉地与我争吵，以使我能真实地看到什么维系着这个信念，好吗？"}, {"id": "310-5", "participant": "来访者", "text": "好的。"}, {"id": "310-6", "participant": "治疗师", "text": "好，从你开始，说“因为我没有全得A，我不适当。\""}, {"id": "310-7", "participant": "来访者", "text": "我不适当，因为我没有全得A。"}, {"id": "310-8", "participant": "治疗师", "text": "不，我不是不适当，我有一个我不适当的信念，但是大多数时间我是合情合理地适当的。"}, {"id": "310-9", "participant": "来访者", "text": "不，我不适当，如果我真的适当，上学期我该全得A。"}, {"id": "310-10", "participant": "治疗师", "text": "那不是事实，适当不等于绝对的学业优秀，如采这是真的，世界上仅有1%的人算是遗当，其他任何人都不适当。"}"""
output_str=r"""[
  {
    "id": "310-0",
    "participant": "治疗师",
    "text": "因为上学期在学校里你做得不如你本该做得那么好，所以你不合格，从你所说的，听起来你仍然有一些程度地相信自己。",
    "reason": "相信自己"
  },
  {
    "id": "310-1",
    "participant": "来访者",
    "text": "是的。",
    "reason": "删除引号"
  },
  {
    "id": "310-2",
    "participant": "治疗师",
    "text": "我想得到更好一点的理由，你还有什么依据支持你的信念？",
    "reason": ""
  },
  {
    "id": "310-3",
    "participant": "来访者",
    "text": "可以。",
    "reason": "删除引号"
  },
  {
    "id": "310-4",
    "participant": "治疗师",
    "text": "我想做的是角色扮演，我扮演你心理上的“理性”部分，即理性的自尊。仅仅因为你未能全得A，并不意味着你就是彻头彻尾的不合格，我想让你扮演你心理上的情绪部分，你仍然真实地相信你不合格，这是来自于你心里的声音。我想让你尽可能严厉地与我争吵，以使我能真实地看到什么维系着这个信念，好吗？",
    "reason": "知遵->自尊 地->的 添加句号 删除· 删除，"
  },
  {
    "id": "310-5",
    "participant": "来访者",
    "text": "好的。",
    "reason": ""
  },
  {
    "id": "310-6",
    "participant": "治疗师",
    "text": "好，从你开始，说“因为我没有全得A，我不适当。”",
    "reason": "“->”"
  },
  {
    "id": "310-7",
    "participant": "来访者",
    "text": "我不适当，因为我没有全得A。",
    "reason": ""
  },
  {
    "id": "310-8",
    "participant": "治疗师",
    "text": "不，我不是不适当，我有一个我不适当的信念，但是大多数时间我是合情合理地适当的。",
    "reason": ""
  },
  {
    "id": "310-9",
    "participant": "来访者",
    "text": "不，我不适当，如果我真的适当，上学期我该全得A。",
    "reason": ""
  },
  {
    "id": "310-10",
    "participant": "治疗师",
    "text": "那不是事实，适当不等于绝对的学业优秀，如果这是真的，世界上仅有1%的人算是适当，其他任何人都不适当。",
    "reason": "如采->如果 遗当->适当”"
  }
]
"""

input_str2='[{"id": "312-0", "participant": "治疗师", "text": "你是否认识你认为有与你同样信念的其他什么人，“如果我不势力工作，我就会失败，？"}, {"id": "312-1", "participant": "来访者", "text": "我可以肯定我的期友唐娜从高中起就那样认为，地总是日目夜夜的学习。"}, {"id": "312-2", "participant": "治疗师", "text": "你认为那个信念适合她的准确性如何？"}]'
output_str2=r"""[
  {
    "id": "312-0",
    "participant": "治疗师",
    "text": "你是否认识你认为有与你同样信念的其他什么人，有着同样的想法：“如果我不势力工作，我就会失败？”",
    "reasoning": "有着同样想想法 删除逗号"
  },
  {
    "id": "312-1",
    "participant": "来访者",
    "text": "我可以肯定我的朋友唐娜从高中起就那样认为，她总是日夜兼程地学习。",
    "reasoning": "日夜兼程"
  },
  {
    "id": "312-2",
    "participant": "治疗师",
    "text": "你认为那个信念适合她的准确性如何？",
    "reasoning": ""
  }
]
"""

input_str3=r"""[{"id": "310-20", "participant": "来访者", "text": "好的。n转换角色给来访者提供了一个正如治疗师模拟的表达理性论点的机会。治疗师运用来访者使用的相同情感理由，也努力用同样的话。使便用来访者自己的讲话，不加入新的素材，有助干帮助患老对其特定的事精反应更加精确。"}]"""
output_str3=r"""[{"id": "310-20", "participant": "来访者", "text": "好的。","reason":"删除n 转换角色给来访者提供了一个正如治疗师模拟的表达理性论点的机会。治疗师运用来访者使用的相同情感理由，也努力用同样的话。使便用来访者自己的讲话，不加入新的素材，有助干帮助患老对其特定的事精反应更加精确。"}]"""


instruct_prompt=r"请你帮我纠正下面这段心理咨询对话OCR后的结果，以json数组形式输入，以json数组的形式输出:"