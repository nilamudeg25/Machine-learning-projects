import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("matches.csv")

print(df.info())

print("Total no.of rows & column:",df.shape)

#print(df.describe)

#a=df.drop(["umpire3"],axis=1)
#print(a)


#print Total number of matches won by each Team (sort according to id)

#print("Winner Team:",df.winner.unique())

df_winner=df.groupby("winner")[['id']].count()
df_winner=df_winner.sort_values('id',ascending=False).reset_index()
df_winner.rename(columns={'id':'wins','winner':'Teams'},inplace=True)
print("\nTotal matches won by Team:\n",df_winner)

plt.xlabel('Wins',fontweight='bold',fontsize=20)
plt.ylabel('Teams',fontweight='bold',fontsize=20)
plt.tick_params(labelsize=7.5)
#plt.xticks(rotation=90)
plt.title("Matches won by each team",fontsize=35,color="#ad506f")
#plt.bar(df_winner.Teams,df_winner.wins,width=0.3,color=["#eb4034","#ebe534","#5d9e24","#249e8c","#249e8c","#24679e","#65249e","#9e249c","#662344"])
plt.barh(df_winner.Teams,df_winner.wins,color=["#eb4034","#ebe534","#5d9e24","#249e8c","#249e8c","#24679e","#65249e","#9e249c","#662344"])
         

for i,j in enumerate(df_winner.wins):
    plt.text(j+3,i+.25,str(j))
plt.show()  


#season with the most number of matches

df_season=df.groupby("season")[['id']].count()
df_season=df_season.sort_values('id',ascending=False).reset_index()
df_season.rename(columns={'id':'Matches','season':'Year'},inplace=True)
print("\nMost no. of matches with season:\n",df_season)


plt.xlabel('Year',fontweight='bold',fontsize=20)
plt.ylabel('Matches',fontweight='bold',fontsize=20)
plt.tick_params(labelsize=10)
plt.title("Season with most number of Matches",fontsize=35,color="#74c716",fontweight='bold')
plt.plot(df_season.Year,df_season.Matches,"D-.r")

for i,j in zip(df_season.Year,df_season.Matches):
    plt.text(i,j,"({},{})".format(i,j))
plt.show()



# which venue hosted the most no.of matches

venue=df.venue.unique()
print("\nTotal no of venue:\n",len(venue))

venue=df.groupby("venue")[['id']].count()
venue=venue.sort_values('id',ascending=False).reset_index()
venue.rename(columns={'id':'Total','venue':'Stadium'},inplace=True)
print(venue)

plt.xlabel('Total',fontweight='bold',fontsize=20)
plt.ylabel('Stadium',fontweight='bold',fontsize=20)
plt.title("Venue Hosted The Most Number Of Matches",fontweight="bold",fontsize=20,color="#d63e36")
plt.tick_params(labelsize=8)
plt.scatter(venue.Total,venue.Stadium,color="#58d636")
for i,j in enumerate(venue.Total):
    plt.text(j+3,i+.25,str(j))
plt.show()



"""
print(df["winner"].head(10))
print(df["winner"].tail(10))
print(df["city"])

print(df.iloc[2])

print(df.head())
print(df.tail())

b=df.drop([1])
print(b)

c=df.iloc[51,7]
print(c)


print(df.iloc[2:11])


df1=df.dropna()
print(df1)

df4=df["umpire2"].dropna()
print(df4)

df2=df.fillna(0)
print(df2)

df3=df["umpire3"].fillna(0)
print(df3)


df5=df[(df["win_by_runs"]>=50) & (df["win_by_runs"]<=35)]
print(df5)


df5=pd.isnull(df["umpire2"])
print("null value:",df[df5])

data=df[df["season"]>2016]
print(data)

"""


