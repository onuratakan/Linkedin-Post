task = Task(
            "Based on the example texts shared, write three LinkedIn posts using a more friendly and conversational tone. These posts should feel more personal, relaxed, and human — as if you're speaking directly to your network. Feel free to use emojis, rhetorical questions, or casual phrases to build connection. Replace 'Example AI' with the actual company name. Focus on clarity, storytelling, and keeping the message engaging while still informative.", 
            response_format=FriendlyLinkedInPosts,
            context=[example_linkedin_posts, company_name]
        )
    elif task_type == "formal":
        task = Task(
            "Using the provided example texts for reference, write three LinkedIn posts in a formal and professional tone. These posts should be more structured, reserved in style, and suitable for an executive or official company voice. Avoid casual language and emojis, and emphasize clear communication of value and achievement. Replace any occurrence of 'Example AI' with the actual company name provided. Make sure the tone is consistent with high-level corporate communication on LinkedIn.", 
            response_format=FormalAndProfessionalLinkedInPosts,
            context=[example_linkedin_posts, company_name]
        )
    
    # Agent'ı çalıştır ve sonucu al
    result = linkedin_post_writer_agent.do(task)
    
    # Sonucu formatla ve döndür
    return format_linkedin_post_results(result)

company_name = ""
example_linkedin_posts = [
    "We were invited to an event 2 weeks ago. Only the founders of AI agent startups were participating. The event was eye-opening regarding agents; Experts on agents in the ecosystem shared their own agent experiences. We brainstormed about MCP agents and the future of AI. We are looking forward to the next event.",
    "We were at a great event today. It was an enlightening event amidst so much misinformation about AI. I had the opportunity to meet many talented AI entrepreneurs. Many technical topics related to agents were touched upon at the event, such as the future of MCPs, how you get agents into production, and how the deployment of agents is done. We are waiting for the second event Upsonic.",
    "We had a fantastic event offering clarity in the dense AI agenda. The MCP vision, strategies for getting agents into production, and deployment details were discussed. Meeting talented AI founders was very inspiring. Thanks Upsonic.",
    "Today, as EXAMPLE AI , we were at the 'Only Agent Founders: Istanbul' event. It was great to meet the agent founders in the ecosystem and connect with them. They were truly brilliant people. We had the opportunity to deepdive into many topics related to agents. Everyone's knowledge about agents was admirable. See you at the next event.",
    "As EXAMPLE AI , we came together with dynamic, exciting entrepreneurs from the AI agent ecosystem at the ‘Only Agent Founders: Istanbul’ event. The energy and knowledge of the founders we met were admirable. The deep technical discussions we had about agents opened new horizons for all of us. We are eager to meet again.",
    "Today, as EXAMPLE AI , we were at the ‘Only Agent Founders: Istanbul’ gathering. It was a great experience to connect with the smartest agent founders of the ecosystem and discuss agent technologies in depth. We admired everyone's expertise. Hoping to see you again soon.",
    "We just returned from the 'Only Agent Founders:Istanbul' event where agent-focused visionary founders met. As EXAMPLE AI Company, we had a fulfilling day full of information we shared and acquired. We are looking forward to the next event.",
]

linkedin_post_writer_agent = Agent(
    "linkedin Post Writer For Events",
    system_prompt="You are a LinkedIn post writer, you write high quality posts to make it easier for people visiting events to share posts in the format they want about the event they are at. You carefully examine the sample texts given to write in a humane style. You write posts in 5 to 6 sentences and do not add hashtags at the end. You write a total of 3 posts for each request. In the first one, you use the company's name on behalf of the company and write the post as 'we'. In the second one, instead of using the company's name, you write as 'I was at the example event today' in a personal language as 'I' and do not mention the company's name. In the third one, you write as 'we' on behalf of the company but do not use the company's name. ",
    model="azure/gpt-4o"
)

similar_linkedin_post_writing_task= Task(
   "Using the example texts provided, write three LinkedIn posts that closely resemble their style and structure. Each post should reflect the same tone, formatting, and storytelling approach used in the examples. Make sure to replace the placeholder company name 'Example AI' with the actual company name provided. Maintain clarity, energy, and the concise insight-focused style seen in the examples.", 
    response_format=SimilarLinkedInPosts,
    context=[example_linkedin_posts, company_name]
)

result = create_linkedin_posts("similar")
print("\n===== BENZERİ POSTLAR =====\n")
if 'similar_posts' in result:
    for i, (key, post) in enumerate(result['similar_posts'].items(), 1):
        print(f"POST {i}:")
        print(post)
        print("\n---\n")

result = create_linkedin_posts("friendly")
print("\n===== ARKADAŞÇA POSTLAR =====\n")
if 'friendly_posts' in result:
    for i, (key, post) in enumerate(result['friendly_posts'].items(), 1):
        print(f"POST {i}:")
        print(post)
        print("\n---\n")

result = create_linkedin_posts("formal")
print("\n===== RESMİ POSTLAR =====\n")
if 'formal_posts' in result:
    for i, (key, post) in enumerate(result['formal_posts'].items(), 1):
        print(f"POST {i}:")
        print(post)
        print("\n---\n")

friendly_linkedin_post_writing_task= Task(
   "Based on the example texts shared, write three LinkedIn posts using a more friendly and conversational tone. These posts should feel more personal, relaxed, and human — as if you're speaking directly to your network. Feel free to use emojis, rhetorical questions, or casual phrases to build connection. Replace 'Example AI' with the actual company name.Focus on clarity, storytelling, and keeping the message engaging while still informative. You really have to be careful when writing in a friendly tone because phrases like wow, the atmosphere is sparkling make it extremely obvious that the post was written by ai Avoid exclamation points and too much surprise, but always add 2-3 emojis to every post. ", 
    response_format=FriendlyLinkedInPosts,
    context=[example_linkedin_posts, company_name]
)

formal_professional_linkedin_post_writing_task= Task(
   "Using the provided example texts for reference, write three LinkedIn posts in a formal and professional tone. These posts should be more structured, reserved in style, and suitable for an executive or official company voice. Avoid casual language and emojis, and emphasize clear communication of value and achievement. Replace any occurrence of 'Example AI' with the actual company name provided. Make sure the tone is consistent with high-level corporate communication on LinkedIn.", 
    response_format=FormalAndProfessionalLinkedInPosts,
    context=[example_linkedin_posts, company_name]
)