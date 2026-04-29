#!/usr/bin/env python3
import re

summaries = {
    1: "Google I/O 大会将于5月举行，CNET预测本次大会的重点包括：Android XR智能眼镜将从概念走向产品化（去年I/O已展示原型），Gemini大模型将深度集成到Android系统，以及新一代AI助手功能。值得注意的是，本次大会是Google展示其AI战略的重要窗口，预计还有多项硬件和软件层面的AI更新值得关注。",
    2: "Google Cloud Next 2026大会在拉斯维加斯开幕，Alphabet宣布了多项AI战略举措：与Nvidia扩大AI合作、推出新一代AI专用芯片、以及面向企业的AI技术栈更新。会议传递的核心信息是Google正在全力押注Agentic AI，将其作为未来云计算和商业AI的核心方向。",
    3: "Google Cloud在Next大会上宣布两款新AI芯片和重大技术栈更新，全面押注Agentic AI。除了硬件层面的AI训练/推理芯片升级，Google还更新了企业级AI开发和部署工具链，旨在帮助企业更便捷地构建和运行AI Agent应用。Cloud Next大会已成为Google展示其AI基础设施能力的年度标志性活动。",
    4: "AWS宣布已在其云平台上提供OpenAI最新的AI产品和服务，这是继微软与OpenAI深度绑定之后，亚马逊在AI竞争中的最新布局。微软同时也在推进基于Claude的新一代Agent产品，显示出各大云厂商正在积极构建多元化的AI模型合作生态，打破单一供应商的垄断格局。",
    5: "OpenAI与微软再次调整合作关系，取消了最后一个Azure排他性条款。现协议仍规定OpenAI产品优先在Azure发布，但微软可以选择放弃该排他性权益。此举被普遍解读为OpenAI为IPO铺路，正在降低对单一合作伙伴的依赖，在微软之外寻求更广泛的云服务商合作。",
    6: "Google翻译新增AI驱动的发音练习功能，可实时分析并纠正用户发音，帮助学习新语言。该功能利用语音识别和AI反馈机制，为语言学习者提供更精准的口语指导。这是Google将AI能力融入其核心产品线的又一案例，翻译工具从文字交流扩展到了口语练习场景。",
    7: "Anthropic宣布Claude已支持直接连接用户个人应用，包括Spotify、Uber Eats和TurboTax等。这意味着Claude不仅能进行对话，还能代你操作真实生活中的服务——比如播放音乐、点外卖或处理税务。这项应用连接器功能已向所有Claude用户开放，标志着大语言模型向真正AI助手演进的又一重要里程碑。",
    8: "三星首款智能眼镜产品已遭泄露，知情人士称该产品将与Ray-Ban Meta智能眼镜竞争，预计今年晚些时候发布。第二代带显示屏版本则计划2027年推出。该产品有望在Google I/O大会上进一步曝光，泄密信息显示三星正积极布局AI可穿戴设备赛道，智能眼镜已成科技巨头们的必争之地。"
}

for i, desc in summaries.items():
    with open(f'{i}.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'<div class="summary-text">.*?</div>',
        f'<div class="summary-text">{desc}</div>',
        content,
        flags=re.DOTALL
    )
    
    with open(f'{i}.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {i}.html")