from langchain_text_splitters import CharacterTextSplitter

text = """
Whispering shadows dance across the silvered horizon as twilight embraces the quiet valley. Somewhere in the distance, an ancient clock chimes three times, reverberating through autumn air crisp with the scent of pine and pinecones. A lone traveler pauses by the moss-covered stone bridge, pulling a wool coat tight against the gathering chill, contemplating the winding path that stretches toward the unknown stars above.
"""

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=""
)

result = splitter.split_text(text)
print(result)