from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun, AskNewsSearch, YahooFinanceNewsTool
from langchain_community.utilities import WikipediaAPIWrapper, AskNewsAPIWrapper
from langchain.tools import Tool 
from datetime import datetime

def save_to_file(data: str, filename: str = "research_findings.txt"):
	timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	formatted_text = f'--- Research Findings ---\nTimestamp: {timestamp}\n\n{data}\n\n'

	with open(filename, "a", encoding='utf-8') as f:
		f.write(formatted_text)
	
	return f'Data successfully written to {filename}'

save_tool = Tool(
	name='save',
	func=save_to_file,
	description='Saves structured data to a text file'
)

def today_date(data: str):
	return datetime.now()

date_tool = Tool(
	name='date',
	func=today_date,
	description='Gets the current date and time in datetime object format'
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
	name="search",
	func=search.run,
	description="search the web for information",
)

wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki_api_wrapper)

asknews_api_wrapper = AskNewsAPIWrapper(asknews_client_id='90965c03-9e72-4723-a7f3-4c2a10bf9f53', asknews_client_secret='xactvpnuW3.o736S3D2~goA2BG')
asknews_tool = AskNewsSearch(api_wrapper=asknews_api_wrapper)
# asknews_tool = Tool(
# 	name="asknews",
# 	func=asknews.run,
# 	description="This tool allows you to perform a search on up-to-date news and historical news. If you needs news from more than 48 hours ago, you can estimate the number of hours back to search."

# )

yahoo_fin_news = YahooFinanceNewsTool()
yahoo_news_tool = Tool(
	name="YahooNews",
	func=yahoo_fin_news.run,
	description="Useful for when you need to find any news in general and financial news in particular. Input should be a company ticker. For example, AAPL for Apple, MSFT for Microsoft."
)


