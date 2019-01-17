tweet = input('Geef tweet: ')

i_hashtag = tweet.find('#')

while i_hashtag != -1:
    # tweet afknippen net na het #-teken
    tweet = tweet[i_hashtag + 1:]
    i_spatie = tweet.find(' ')

    # hashtag uitknippen (en printen)
    print(tweet[:i_spatie])

    #terug op zoek naar een #
    i_hashtag = tweet.find('#')