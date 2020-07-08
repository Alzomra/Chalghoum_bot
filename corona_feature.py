@client.command()
async def corona (ctx,*,country):
        page = requests.get("https://www.worldometers.info/coronavirus/")
        infos = page.text
        info = BeautifulSoup(infos ,'html.parser')
        body = info.find('tbody')
        table= info.find('table')
        col=[]
        for th in table.find_all('th') : 
          col.append((th.text.strip(),[]))


        for tr in body.find_all('tr', {'class' : '' }) :
         i=0
         for td in tr.find_all('td') : 
                col[i][1].append(td.text.strip()) 
                i+=1   

        Dict={title:column for (title,column) in col}
        df=pd.DataFrame(Dict)
        df = df.drop(['Continent', '1 Caseevery X ppl','1 Deathevery X ppl', '1 Testevery X ppl', 'Tests/\n1M pop' , 'Serious,Critical','Tot Cases/1M pop','Deaths/1M pop'], axis = 1)
        df.set_index('#', inplace=True)
        value = df.loc[df['Country,Other'] == country]
        value = value.iloc[0]
        await ctx.send(f'{value.to_string()}')