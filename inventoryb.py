import re

inv_raw = """
001
Five-character-ancient-verse
Zhang Jiuling
THOUGHTS I
A lonely swan from the sea flies,
To alight on puddles it does not deign.
Nesting in the poplar of pearls
It spies and questions green birds twain:
"Don't you fear the threat of slings,
Perched on top of branches so high?
Nice clothes invite pointing fingers,
High climbers god's good will defy.
Bird-hunters will crave me in vain,
For I roam the limitless sky."
002
Five-character-ancient-verse
Zhang Jiuling
ORCHID AND ORANGE I
Tender orchid-leaves in spring
And cinnamon- blossoms bright in autumn
Are as self- contained as life is,
Which conforms them to the seasons.
Yet why will you think that a forest-hermit,
Allured by sweet winds and contented with beauty,
Would no more ask to-be transplanted
THan Would any other natural flower?
003
Five-character-ancient-verse
Zhang Jiuling
THOUGHTS III
The hermit in his lone abode
Nurses his thoughts cleansed of care,
Them he projects to the wild goose
For it to his distant Sovereign to bear.
Who will be moved by the sincerity
Of my vain day-and-night prayer?
What comfort is for my loyalty
When fliers and sinkers can compare?
004
Five-character-ancient-verse
Zhang Jiuling
ORCHID AND ORANGE II
Here, south of the Yangzi, grows a red orangetree.
All winter long its leaves are green,
Not because of a warmer soil,
But because its' nature is used to the cold.
Though it might serve your honourable guests,
You leave it here, far below mountain and river.
Circumstance governs destiny.
Cause and effect are an infinite cycle.
You plant your peach-trees and your plums,
You forget the shade from this other tree.
005
Five-character-ancient-verse
Li Bai
DOWN ZHONGNAN MOUNTAIN
TO THE KIND PILLOW AND BOWL OF HUSI
Down the blue mountain in the evening,
Moonlight was my homeward escort.
Looking back, I saw my path
Lie in levels of deep shadow....
I was passing the farm-house of a friend,
When his children called from a gate of thorn
And led me twining through jade bamboos
Where green vines caught and held my clothes.
And I was glad of a chance to rest
And glad of a chance to drink with my friend....
We sang to the tune of the wind in the pines;
And we finished our songs as the stars went down,
When, I being drunk and my friend more than happy,
Between us we forgot the world.
006
Five-character-ancient-verse
Li Bai
DRINKING ALONE WITH THE MOON
From a pot of wine among the flowers
I drank alone. There was no one with me --
Till, raising my cup, I asked the bright moon
To bring me my shadow and make us three.
Alas, the moon was unable to drink
And my shadow tagged me vacantly;
But still for a while I had these friends
To cheer me through the end of spring....
I sang. The moon encouraged me.
I danced. My shadow tumbled after.
As long as I knew, we were boon companions.
And then I was drunk, and we lost one another.
...Shall goodwill ever be secure?
I watch the long road of the River of Stars.
007
Five-character-ancient-verse
Li Bai
IN SPRING
Your grasses up north are as blue as jade,
Our mulberries here curve green-threaded branches;
And at last you think of returning home,
Now when my heart is almost broken....
O breeze of the spring, since I dare not know you,
Why part the silk curtains by my bed?
008
Five-character-ancient-verse
Du Fu
A VIEW OF TAISHAN
What shall I say of the Great Peak? --
The ancient dukedoms are everywhere green,
Inspired and stirred by the breath of creation,
With the Twin Forces balancing day and night.
...I bare my breast toward opening clouds,
I strain my sight after birds flying home.
When shall I reach the top and hold
All mountains in a single glance?
009
Five-character-ancient-verse
Du Fu
TO MY RETIRED FRIEND WEI
It is almost as hard for friends to meet
As for the morning and evening stars.
Tonight then is a rare event,
Joining, in the candlelight,
Two men who were young not long ago
But now are turning grey at the temples.
...To find that half our friends are dead
Shocks us, burns our hearts with grief.
We little guessed it would be twenty years
Before I could visit you again.
When I went away, you were still unmarried;
But now these boys and girls in a row
Are very kind to their father's old friend.
They ask me where I have been on my journey;
And then, when we have talked awhile,
They bring and show me wines and dishes,
Spring chives cut in the night-rain
And brown rice cooked freshly a special way.
...My host proclaims it a festival,
He urges me to drink ten cups --
But what ten cups could make me as drunk
As I always am with your love in my heart?
...Tomorrow the mountains will separate us;
After tomorrow-who can say?
010
Five-character-ancient-verse
Du Fu
ALONE IN HER BEAUTY
Who is lovelier than she?
Yet she lives alone in an empty valley.
She tells me she came from a good family
Which is humbled now into the dust.
...When trouble arose in the Kuan district,
Her brothers and close kin were killed.
What use were their high offices,
Not even shielding their own lives? --
The world has but scorn for adversity;
Hope goes out, like the light of a candle.
Her husband, with a vagrant heart,
Seeks a new face like a new piece of jade;
And when morning-glories furl at night
And mandarin-ducks lie side by side,
All he can see is the smile of the new love,
While the old love weeps unheard.
The brook was pure in its mountain source,
But away from the mountain its waters darken.
...Waiting for her maid to come from selling pearls
For straw to cover the roof again,
She picks a few flowers, no longer for her hair,
And lets pine-needles fall through her fingers,
And, forgetting her thin silk sleeve and the cold,
She leans in the sunset by a tall bamboo.
011
Five-character-ancient-verse
Du Fu
SEEING Li Bai IN A DREAM I
There are sobs when death is the cause of parting;
But life has its partings again and again.
...From the poisonous damps of the southern river
You had sent me not one sign from your exile --
Till you came to me last night in a dream,
Because I am always thinking of you.
I wondered if it were really you,
Venturing so long a journey.
You came to me through the green of a forest,
You disappeared by a shadowy fortress....
Yet out of the midmost mesh of your snare,
How could you lift your wings and use them?
...I woke, and the low moon's glimmer on a rafter
Seemed to be your face, still floating in the air.
...There were waters to cross, they were wild and tossing;
If you fell, there were dragons and rivermonsters.
012
Five-character-ancient-verse
Du Fu
SEEING Li Bai IN A DREAM II
This cloud, that has drifted all day through the sky,
May, like a wanderer, never come back....
Three nights now I have dreamed of you --
As tender, intimate and real as though I were awake.
And then, abruptly rising to go,
You told me the perils of adventure
By river and lake-the storms, the wrecks,
The fears that are borne on a little boat;
And, here in my doorway, you rubbed your white head
As if there were something puzzling you.
...Our capital teems with officious people,
While you are alone and helpless and poor.
Who says that the heavenly net never fails?
It has brought you ill fortune, old as you are.
...A thousand years' fame, ten thousand years' fameWhat good, when you are dead and gone.
013
Five-character-quatrain
Wang Wei
AT PARTING
I dismount from my horse and I offer you wine,
And I ask you where you are going and why.
And you answer: "I am discontent
And would rest at the foot of the southern mountain.
So give me leave and ask me no questions.
White clouds pass there without end."
014
Five-character-quatrain
Wang Wei
TO QIWU QIAN BOUND HOME
AFTER FAILING IN AN EXAMINATION
In a happy reign there should be no hermits;
The wise and able should consult together....
So you, a man of the eastern mountains,
Gave up your life of picking herbs
And came all the way to the Gate of Gold --
But you found your devotion unavailing.
...To spend the Day of No Fire on one of the southern rivers,
You have mended your spring clothes here in these northern cities.
I pour you the farewell wine as you set out from the capital --
Soon I shall be left behind here by my bosomfriend.
In your sail-boat of sweet cinnamon-wood
You will float again toward your own thatch door,
Led along by distant trees
To a sunset shining on a far-away town.
...What though your purpose happened to fail,
Doubt not that some of us can hear high music.
015
Five-character-quatrain
Wang Wei
A GREEN STREAM
I have sailed the River of Yellow Flowers,
Borne by the channel of a green stream,
Rounding ten thousand turns through the mountains
On a journey of less than thirty miles....
Rapids hum over heaped rocks;
But where light grows dim in the thick pines,
The surface of an inlet sways with nut-horns
And weeds are lush along the banks.
...Down in my heart I have always been as pure
As this limpid water is....
Oh, to remain on a broad flat rock
And to cast a fishing-line forever!
016
Five-character-quatrain
Wang Wei
A FARM-HOUSE ON THE WEI RIVER
In the slant of the sun on the country-side,
Cattle and sheep trail home along the lane;
And a rugged old man in a thatch door
Leans on a staff and thinks of his son, the herdboy.
There are whirring pheasants? full wheat-ears,
Silk-worms asleep, pared mulberry-leaves.
And the farmers, returning with hoes on their shoulders,
Hail one another familiarly.
...No wonder I long for the simple life
And am sighing the old song, Oh, to go Back Again!
017
Five-character-quatrain
Wang Wei
THE BEAUTIFUL XI SHI
Since beauty is honoured all over the Empire,
How could Xi Shi remain humbly at home? --
Washing clothes at dawn by a southern lake --
And that evening a great lady in a palace of the north:
Lowly one day, no different from the others,
The next day exalted, everyone praising her.
No more would her own hands powder her face
Or arrange on her shoulders a silken robe.
And the more the King loved her, the lovelier she looked,
Blinding him away from wisdom.
...Girls who had once washed silk beside her
Were kept at a distance from her chariot.
And none of the girls in her neighbours' houses
By pursing their brows could copy her beauty.
018
Five-character-ancient-verse
Meng Haoran
ON CLIMBING ORCHID MOUNTAIN
IN THE AUTUMN TO ZHANG
On a northern peak among white clouds
You have found your hermitage of peace;
And now, as I climb this mountain to see you,
High with the wildgeese flies my heart.
The quiet dusk might seem a little sad
If this autumn weather were not so brisk and clear;
I look down at the river bank, with homeward-bound villagers
Resting on the sand till the ferry returns;
There are trees at the horizon like a row of grasses
And against the river's rim an island like the moon
I hope that you will come and meet me, bringing a basket of wine --
And we'll celebrate together the Mountain Holiday.
019
Five-character-ancient-verse
Meng Haoran
IN SUMMER AT THE SOUTH PAVILION
THINKING OF XING
The mountain-light suddenly fails in the west,
In the east from the lake the slow moon rises.
I loosen my hair to enjoy the evening coolness
And open my window and lie down in peace.
The wind brings me odours of lotuses,
And bamboo-leaves drip with a music of dew....
I would take up my lute and I would play,
But, alas, who here would understand?
And so I think of you, old friend,
O troubler of my midnight dreams !
020
Five-character-ancient-verse
Meng Haoran
AT THE MOUNTAIN-LODGE OF THE BUDDHIST PRIEST YE
WAITING IN VAIN FOR MY FRIEND DING
Now that the sun has set beyond the western range,
Valley after valley is shadowy and dim....
And now through pine-trees come the moon and the chill of evening,
And my ears feel pure with the sound of wind and water
Nearly all the woodsmen have reached home,
Birds have settled on their perches in the quiet mist....
And still -- because you promised -- I am waiting for you, waiting,
Playing lute under a wayside vine.
021
Five-character-ancient-verse
Wang Changling
WITH MY BROTHER AT THE SOUTH STUDY
THINKING IN THE MOONLIGHT OF VICE-PREFECT
CUI IN SHANYIN
Lying on a high seat in the south study,
We have lifted the curtain-and we see the rising moon
Brighten with pure light the water and the grove
And flow like a wave on our window and our door.
It will move through the cycle, full moon and then crescent again,
Calmly, beyond our wisdom, altering new to old.
...Our chosen one, our friend, is now by a limpid river --
Singing, perhaps, a plaintive eastern song.
He is far, far away from us, three hundred miles away.
And yet a breath of orchids comes along the wind.
022
Five-character-ancient-verse
Qiu Wei
AFTER MISSING THE RECLUSE
ON THE WESTERN MOUNTAIN
To your hermitage here on the top of the mountain
I have climbed, without stopping, these ten miles.
I have knocked at your door, and no one answered;
I have peeped into your room, at your seat beside the table.
Perhaps you are out riding in your canopied chair,
Or fishing, more likely, in some autumn pool.
Sorry though I am to be missing you,
You have become my meditation --
The beauty of your grasses, fresh with rain,
And close beside your window the music of your pines.
I take into my being all that I see and hear,
Soothing my senses, quieting my heart;
And though there be neither host nor guest,
Have I not reasoned a visit complete?
...After enough, I have gone down the mountain.
Why should I wait for you any longer?
023
Five-character-ancient-verse
Qiwu Qian
A BOAT IN SPRING ON RUOYA LAKE
Thoughtful elation has no end:
Onward I bear it to whatever come.
And my boat and I, before the evening breeze
Passing flowers, entering the lake,
Turn at nightfall toward the western valley,
Where I watch the south star over the mountain
And a mist that rises, hovering soft,
And the low moon slanting through the trees;
And I choose to put away from me every worldly matter
And only to be an old man with a fishing-pole.
024
Five-character-ancient-verse
Chang Jian
AT WANG CHANGLIN' S RETREAT
Here, beside a clear deep lake,
You live accompanied by clouds;
Or soft through the pine the moon arrives
To be your own pure-hearted friend.
You rest under thatch in the shadow of your flowers,
Your dewy herbs flourish in their bed of moss.
Let me leave the world. Let me alight, like you,
On your western mountain with phoenixes and cranes.
025
Five-character-ancient-verse
Cen Can
ASCENDING THE PAGODA AT THE TEMPLE OF KIND
FAVOUR WITH GAO SHI AND XUE JU
The pagoda, rising abruptly from earth,
Reaches to the very Palace of Heaven....
Climbing, we seem to have left the world behind us,
With the steps we look down on hung from space.
It overtops a holy land
And can only have been built by toil of the spirit.
Its four sides darken the bright sun,
Its seven stories cut the grey clouds;
Birds fly down beyond our sight,
And the rapid wind below our hearing;
Mountain-ranges, toward the east,
Appear to be curving and flowing like rivers;
Far green locust-trees line broad roads
Toward clustered palaces and mansions;
Colours of autumn, out of the west,
Enter advancing through the city;
And northward there lie, in five graveyards,
Calm forever under dewy green grass,
Those who know life's final meaning
Which all humankind must learn.
...Henceforth I put my official hat aside.
To find the Eternal Way is the only happiness.
026
Five-character-ancient-verse
Yuan Jie
TO THE TAX-COLLECTORS
AFTER THE BANDITS RETREAT
In the year Kuimao the bandits from Xiyuan entered Daozhou, set fire,
raided, killed, and looted. The whole district was almost ruined. The
next year the bandits came again and, attacking the neighbouring
prefecture, Yong, passed this one by. It was not because we were strong
enough to defend ourselves, but, probably, because they pitied us. And
how now can these commissioners bear to impose extra taxes? I have
written this poem for the collectors' information.
I still remember those days of peace --
Twenty years among mountains and forests,
The pure stream running past my yard,
The caves and valleys at my door.
Taxes were light and regular then,
And I could sleep soundly and late in the morningTill suddenly came a sorry change.
...For years now I have been serving in the army.
When I began here as an official,
The mountain bandits were rising again;
But the town was so small it was spared by the thieves,
And the people so poor and so pitiable
That all other districts were looted
And this one this time let alone.
...Do you imperial commissioners
Mean to be less kind than bandits?
The people you force to pay the poll
Are like creatures frying over a fire.
And how can you sacrifice human lives,
Just to be known as able collectors? --
...Oh, let me fling down my official seal,
Let me be a lone fisherman in a small boat
And support my family on fish and wheat
And content my old age with rivers and lakes!
027
Five-character-ancient-verse
Wei Yingwu
ENTERTAINING LITERARY MEN IN MY
OFFICIAL RESIDENCE ON A RAINY DAY
Outside are insignia, shown in state;
But here are sweet incense-clouds, quietly ours.
Wind and rain, coming in from sea,
Have cooled this pavilion above the lake
And driven the feverish heat away
From where my eminent guests are gathered.
...Ashamed though I am of my high position
While people lead unhappy lives,
Let us reasonably banish care
And just be friends, enjoying nature.
Though we have to go without fish and meat,
There are fruits and vegetables aplenty.
...We bow, we take our cups of wine,
We give our attention to beautiful poems.
When the mind is exalted, the body is lightened
And feels as if it could float in the wind.
...Suzhou is famed as a centre of letters;
And all you writers, coming here,
Prove that the name of a great land
Is made by better things than wealth.
028
Five-character-ancient-verse
Wei Yingwu
SETTING SAIL ON THE YANGZI
TO SECRETARY YUAN
Wistful, away from my friends and kin,
Through mist and fog I float and float
With the sail that bears me toward Loyang.
In Yangzhou trees linger bell-notes of evening,
Marking the day and the place of our parting....
When shall we meet again and where?
...Destiny is a boat on the waves,
Borne to and fro, beyond our will.
029
Five-character-ancient-verse
Wei Yingwu
A POEM TO A TAOIST HERMIT
CHUANJIAO MOUNTAIN
My office has grown cold today;
And I suddenly think of my mountain friend
Gathering firewood down in the valley
Or boiling white stones for potatoes in his hut....
I wish I might take him a cup of wine
To cheer him through the evening storm;
But in fallen leaves that have heaped the bare slopes,
How should I ever find his footprints!
030
Five-character-ancient-verse
Wei Yingwu
ON MEETING MY FRIEND FENG ZHU
IN THE CAPITAL
Out of the east you visit me,
With the rain of Baling still on your clothes,
I ask you what you have come here for;
You say: "To buy an ax for cutting wood in the mountains"
...Hidden deep in a haze of blossom,
Swallow fledglings chirp at ease
As they did when we parted, a year ago....
How grey our temples have grown since them!
031
Five-character-ancient-verse
Wei Yingwu
MOORING AT TWILIGHT IN YUYI DISTRICT
Furling my sail near the town of Huai,
I find for harbour a little cove
Where a sudden breeze whips up the waves.
The sun is growing dim now and sinks in the dusk.
People are coming home. The bright mountain-peak darkens.
Wildgeese fly down to an island of white weeds.
...At midnight I think of a northern city-gate,
And I hear a bell tolling between me and sleep.
032
Five-character-ancient-verse
Wei Yingwu
EAST OF THE TOWN
From office confinement all year long,
I have come out of town to be free this morning
Where willows harmonize the wind
And green hills lighten the cares of the world.
I lean by a tree and rest myself
Or wander up and down a stream.
...Mists have wet the fragrant meadows;
A spring dove calls from some hidden place.
...With quiet surroundings, the mind is at peace,
But beset with affairs, it grows restless again....
Here I shall finally build me a cabin,
As Tao Qian built one long ago.
033
Five-character-ancient-verse
Wei Yingwu
TO MY DAUGHTER
ON HER MARRIAGE INTO THE YANG FAMILY
My heart has been heavy all day long
Because you have so far to go.
The marriage of a girl, away from her parents,
Is the launching of a little boat on a great river.
...You were very young when your mother died,
Which made me the more tender of you.
Your elder sister has looked out for you,
And now you are both crying and cannot part.
This makes my grief the harder to bear;
Yet it is right that you should go.
...Having had from childhood no mother to guide you,
How will you honour your mother-in-law?
It's an excellent family; they will be kind to you,
They will forgive you your mistakes --
Although ours has been so pure and poor
That you can take them no great dowry.
Be gentle and respectful, as a woman should be,
Careful of word and look, observant of good example.
...After this morning we separate,
There's no knowing for how long....
I always try to hide my feelings --
They are suddenly too much for me,
When I turn and see my younger daughter
With the tears running down her cheek.
034
Five-character-ancient-verse
Liu Zongyuan
READING BUDDHIST CLASSICS WITH ZHAO
AT HIS TEMPLE IN THE EARLY MORNING
I clean my teeth in water drawn from a cold well;
And while I brush my clothes, I purify my mind;
Then, slowly turning pages in the Tree-Leaf Book,
I recite, along the path to the eastern shelter.
...The world has forgotten the true fountain of this teaching
And people enslave themselves to miracles and fables.
Under the given words I want the essential meaning,
I look for the simplest way to sow and reap my nature.
Here in the quiet of the priest's templecourtyard,
Mosses add their climbing colour to the thick bamboo;
And now comes the sun, out of mist and fog,
And pines that seem to be new-bathed;
And everything is gone from me, speech goes, and reading,
Leaving the single unison.
035
Five-character-ancient-verse
Liu Zongyuan
DWELLING BY A STREAM
I had so long been troubled by official hat and robe
That I am glad to be an exile here in this wild southland.
I am a neighbour now of planters and reapers.
I am a guest of the mountains and woods.
I plough in the morning, turning dewy grasses,
And at evening tie my fisher-boat, breaking the quiet stream.
Back and forth I go, scarcely meeting anyone,
And sing a long poem and gaze at the blue sky.
036
Folk-song-styled-verse
Wang Changling
AT A BORDER-FORTRESS
Cicadas complain of thin mulberry-trees
In the Eighth-month chill at the frontier pass.
Through the gate and back again, all along the road,
There is nothing anywhere but yellow reeds and grasses
And the bones of soldiers from You and from Bing
Who have buried their lives in the dusty sand.
...Let never a cavalier stir you to envy
With boasts of his horse and his horsemanship
037
Folk-song-styled-verse
Wang Changling
UNDER A BORDER-FORTRESS
Drink, my horse, while we cross the autumn water!-
The stream is cold and the wind like a sword,
As we watch against the sunset on the sandy plain,
Far, far away, shadowy Lingtao.
Old battles, waged by those long walls,
Once were proud on all men's tongues.
But antiquity now is a yellow dust,
Confusing in the grasses its ruins and white bones.
038
Folk-song-styled-verse
Li Bai
THE MOON AT THE FORTIFIED PASS
The bright moon lifts from the Mountain of Heaven
In an infinite haze of cloud and sea,
And the wind, that has come a thousand miles,
Beats at the Jade Pass battlements....
China marches its men down Baideng Road
While Tartar troops peer across blue waters of the bay....
And since not one battle famous in history
Sent all its fighters back again,
The soldiers turn round, looking toward the border,
And think of home, with wistful eyes,
And of those tonight in the upper chambers
Who toss and sigh and cannot rest.
039
Folk-song-styled-verse
Li Bai
BALLADS OF FOUR SEASONS: SPRING
The lovely Lo Fo of the western land
Plucks mulberry leaves by the waterside.
Across the green boughs stretches out her white hand;
In golden sunshine her rosy robe is dyed.
"my silkworms are hungry, I cannot stay.
Tarry not with your five-horse cab, I pray."
040
Folk-song-styled-verse
Li Bai
BALLADS OF FOUR SEASONS: SUMMER
On Mirror Lake outspread for miles and miles,
The lotus lilies in full blossom teem.
In fifth moon Xi Shi gathers them with smiles,
Watchers o'erwhelm the bank of Yuoye Stream.
Her boat turns back without waiting moonrise
To yoyal house amid amorous sighs.
041
Folk-song-styled-verse
Li Bai
A SONG OF AN AUTUMN MIDNIGHT
A slip of the moon hangs over the capital;
Ten thousand washing-mallets are pounding;
And the autumn wind is blowing my heart
For ever and ever toward the Jade Pass....
Oh, when will the Tartar troops be conquered,
And my husband come back from the long campaign!
042
Folk-song-styled-verse
Li Bai
BALLADS OF FOUR SEASONS: WINTER
The courier will depart next day, she's told.
She sews a warrior's gown all night.
Her fingers feel the needle cold.
How can she hold the scissors tight?
The work is done, she sends it far away.
When will it reach the town where warriors stay?
043
Folk-song-styled-verse
Li Bai
A SONG OF CHANGGAN
My hair had hardly covered my forehead.
I was picking flowers, paying by my door,
When you, my lover, on a bamboo horse,
Came trotting in circles and throwing green plums.
We lived near together on a lane in Ch'ang-kan,
Both of us young and happy-hearted.
...At fourteen I became your wife,
So bashful that I dared not smile,
And I lowered my head toward a dark corner
And would not turn to your thousand calls;
But at fifteen I straightened my brows and laughed,
Learning that no dust could ever seal our love,
That even unto death I would await you by my post
And would never lose heart in the tower of silent watching.
...Then when I was sixteen, you left on a long journey
Through the Gorges of Ch'u-t'ang, of rock and whirling water.
And then came the Fifth-month, more than I could bear,
And I tried to hear the monkeys in your lofty far-off sky.
Your footprints by our door, where I had watched you go,
Were hidden, every one of them, under green moss,
Hidden under moss too deep to sweep away.
And the first autumn wind added fallen leaves.
And now, in the Eighth-month, yellowing butterflies
Hover, two by two, in our west-garden grasses
And, because of all this, my heart is breaking
And I fear for my bright cheeks, lest they fade.
...Oh, at last, when you return through the three Pa districts,
Send me a message home ahead!
And I will come and meet you and will never mind the distance,
All the way to Chang-feng Sha.
044
Folk-song-styled-verse
Meng Jiao
A SONG OF A PURE-HEARTED GIRL
Lakka-trees ripen two by two
And mandarin-ducks die side by side.
If a true-hearted girl will love only her husband,
In a life as faithfully lived as theirs,
What troubling wave can arrive to vex
A spirit like water in a timeless well?
045
Folk-song-styled-verse
Meng Jiao
A TRAVELLER'S SONG
The thread in the hands of a fond-hearted mother
Makes clothes for the body of her wayward boy;
Carefully she sews and thoroughly she mends,
Dreading the delays that will keep him late from home.
But how much love has the inch-long grass
For three spring months of the light of the sun?
046
Seven-character-ancient-verse
Chen Ziang
ON A GATE-TOWER AT YUZHOU
Where, before me, are the ages that have gone?
And where, behind me, are the coming generations?
I think of heaven and earth, without limit, without end,
And I am all alone and my tears fall down.
047
Seven-character-ancient-verse
Li Qi
AN OLD AIR
There once was a man, sent on military missions,
A wanderer, from youth, on the You and Yan frontiers.
Under the horses' hoofs he would meet his foes
And, recklessly risking his seven-foot body,
Would slay whoever dared confront
Those moustaches that bristled like porcupinequills.
...There were dark clouds below the hills, there were white clouds
above
them,
But before a man has served full time, how can he go back?
In eastern Liao a girl was waiting, a girl of fifteen years,
Deft with a guitar, expert in dance and song.
...She seems to be fluting, even now, a reed-song of home,
Filling every soldier's eyes with homesick tears.
048
Seven-character-ancient-verse
Li Qi
A FAREWELL TO MY FRIEND CHEN ZHANGFU
In the Fourth-month the south wind blows plains of yellow barley,
Date-flowers have not faded yet and lakka-leaves are long.
The green peak that we left at dawn we still can see at evening,
While our horses whinny on the road, eager to turn homeward.
...Chen, my friend, you have always been a great and good man,
With your dragon's moustache, tiger's eyebrows and your massive
forehead.
In your bosom you have shelved away ten thousand volumes.
You have held your head high, never bowed it in the dust.
...After buying us wine and pledging us, here at the eastern gate,
And taking things as lightly as a wildgoose feather,
Flat you lie, tipsy, forgetting the white sun;
But now and then you open your eyes and gaze at a high lone cloud.
...The tide-head of the lone river joins the darkening sky.
The ferryman beaches his boat. It has grown too late to sail.
And people on their way from Cheng cannot go home,
And people from Loyang sigh with disappointment.
...I have heard about the many friends around your wood land dwelling.
Yesterday you were dismissed. Are they your friends today?
049
Seven-character-ancient-verse
Li Qi
A LUTE SONG
Our host, providing abundant wine to make the night mellow,
Asks his guest from Yangzhou to play for us on the lute.
Toward the moon that whitens the city-wall, black crows are flying,
Frost is on ten thousand trees, and the wind blows through our clothes;
But a copper stove has added its light to that of flowery candles,
And the lute plays The Green Water, and then The Queen of Chu.
Once it has begun to play, there is no other sound:
A spell is on the banquet, while the stars grow thin....
But three hundred miles from here, in Huai, official duties await him,
And so it's farewell, and the road again, under cloudy mountains.
050
Seven-character-ancient-verse
Li Qi
ON HEARING DONG PLAY THE FLAGEOLET
A POEM TO PALACE-ATTENDANT FANG
When this melody for the flageolet was made by Lady Cai,
When long ago one by one she sang its eighteen stanzas,
Even the Tartars were shedding tears into the border grasses,
And the envoy of China was heart-broken, turning back home with his
escort.
...Cold fires now of old battles are grey on ancient forts,
And the wilderness is shadowed with white new-flying snow.
...When the player first brushes the Shang string and the Jue and then
the Yu,
Autumn-leaves in all four quarters are shaken with a murmur.
Dong, the master,
Must have been taught in heaven.
Demons come from the deep pine-wood and stealthily listen
To music slow, then quick, following his hand,
Now far away, now near again, according to his heart.
A hundred birds from an empty mountain scatter and return;
Three thousand miles of floating clouds darken and lighten;
A wildgoose fledgling, left behind, cries for its flock,
And a Tartar child for the mother he loves.
Then river waves are calmed
And birds are mute that were singing,
And Wuzu tribes are homesick for their distant land,
And out of the dust of Siberian steppes rises a plaintive sorrow.
...Suddenly the low sound leaps to a freer tune,
Like a long wind swaying a forest, a downpour breaking tiles,
A cascade through the air, flying over tree-tops.
...A wild deer calls to his fellows. He is running among the mansions
In the corner of the capital by the Eastern Palace wall....
Phoenix Lake lies opposite the Gate of Green Jade;
But how can fame and profit concern a man of genius?
Day and night I long for him to bring his lute again.
051
Seven-character-ancient-verse
Li Qi
ON HEARING AN WANSHAN PLAY THE REED-PIPE
Bamboo from the southern hills was used to make this pipe.
And its music, that was introduced from Persia first of all,
Has taken on new magic through later use in China.
And now the Tartar from Liangzhou, blowing it for me,
Drawing a sigh from whosoever hears it,
Is bringing to a wanderer's eyes homesick tears....
Many like to listen; but few understand.
To and fro at will there's a long wind flying,
Dry mulberry-trees, old cypresses, trembling in its chill.
There are nine baby phoenixes, outcrying one another;
A dragon and a tiger spring up at the same moment;
Then in a hundred waterfalls ten thousand songs of autumn
Are suddenly changing to The Yuyang Lament;
And when yellow clouds grow thin and the white sun darkens,
They are changing still again to Spring in the Willow Trees.
Like Imperial Garden flowers, brightening the eye with beauty,
Are the high-hall candles we have lighted this cold night,
And with every cup of wine goes another round of music.
052
Seven-character-ancient-verse
Meng Haoran
RETURNING AT NIGHT TO LUMEN MOUNTAIN
A bell in the mountain-temple sounds the coming of night.
I hear people at the fishing-town stumble aboard the ferry,
While others follow the sand-bank to their homes along the river.
...I also take a boat and am bound for Lumen Mountain --
And soon the Lumen moonlight is piercing misty trees.
I have come, before I know it, upon an ancient hermitage,
The thatch door, the piney path, the solitude, the quiet,
Where a hermit lives and moves, never needing a companion.
053
Seven-character-ancient-verse
Li Bai
A SONG OF LU MOUNTAIN TO CENSOR LU XUZHOU
I am the madman of the Chu country
Who sang a mad song disputing Confucius.
...Holding in my hand a staff of green jade,
I have crossed, since morning at the Yellow Crane Terrace,
All five Holy Mountains, without a thought of distance,
According to the one constant habit of my life.
Lu Mountain stands beside the Southern Dipper
In clouds reaching silken like a nine-panelled screen,
With its shadows in a crystal lake deepening the green water.
The Golden Gate opens into two mountain-ranges.
A silver stream is hanging down to three stone bridges
Within sight of the mighty Tripod Falls.
Ledges of cliff and winding trails lead to blue sky
And a flush of cloud in the morning sun,
Whence no flight of birds could be blown into Wu.
...I climb to the top. I survey the whole world.
I see the long river that runs beyond return,
Yellow clouds that winds have driven hundreds of miles
And a snow-peak whitely circled by the swirl of a ninefold stream.
And so I am singing a song of Lu Mountain,
A song that is born of the breath of Lu Mountain.
...Where the Stone Mirror makes the heart's purity purer
And green moss has buried the footsteps of Xie,
I have eaten the immortal pellet and, rid of the world's troubles,
Before the lute's third playing have achieved my element.
Far away I watch the angels riding coloured clouds
Toward heaven's Jade City, with hibiscus in their hands.
And so, when I have traversed the nine sections of the world,
I will follow Saint Luao up the Great Purity.
054
Seven-character-ancient-verse
Li Bai
TIANMU MOUNTAIN ASCENDED IN A DREAM
A seafaring visitor will talk about Japan,
Which waters and mists conceal beyond approach;
But Yueh people talk about Heavenly Mother Mountain,
Still seen through its varying deeps of cloud.
In a straight line to heaven, its summit enters heaven,
Tops the five Holy Peaks, and casts a shadow through China
With the hundred-mile length of the Heavenly Terrace Range,
Which, just at this point, begins turning southeast.
...My heart and my dreams are in Wu and Yueh
And they cross Mirror Lake all night in the moon.
And the moon lights my shadow
And me to Yan River --
With the hermitage of Xie still there
And the monkeys calling clearly over ripples of green water.
I wear his pegged boots
Up a ladder of blue cloud,
Sunny ocean half-way,
Holy cock-crow in space,
Myriad peaks and more valleys and nowhere a road.
Flowers lure me, rocks ease me. Day suddenly ends.
Bears, dragons, tempestuous on mountain and river,
Startle the forest and make the heights tremble.
Clouds darken with darkness of rain,
Streams pale with pallor of mist.
The Gods of Thunder and Lightning
Shatter the whole range.
The stone gate breaks asunder
Venting in the pit of heaven,
An impenetrable shadow.
...But now the sun and moon illumine a gold and silver terrace,
And, clad in rainbow garments, riding on the wind,
Come the queens of all the clouds, descending one by one,
With tigers for their lute-players and phoenixes for dancers.
Row upon row, like fields of hemp, range the fairy figures.
I move, my soul goes flying,
I wake with a long sigh,
My pillow and my matting
Are the lost clouds I was in.
...And this is the way it always is with human joy:
Ten thousand things run for ever like water toward the east.
And so I take my leave of you, not knowing for how long.
...But let me, on my green slope, raise a white deer
And ride to you, great mountain, when I have need of you.
Oh, how can I gravely bow and scrape to men of high rank and men of
high
office
Who never will suffer being shown an honest-hearted face!
055
Seven-character-ancient-verse
Li Bai
PARTING AT A WINE-SHOP IN NANJING
A wind, bringing willow-cotton, sweetens the shop,
And a girl from Wu, pouring wine, urges me to share it
With my comrades of the city who are here to see me off;
And as each of them drains his cup, I say to him in parting,
Oh, go and ask this river running to the east
If it can travel farther than a friend's love!
056
Seven-character-ancient-verse
Li Bai
A FAREWELL TO SECRETARY SHUYUN
AT THE XIETIAO VILLA IN XUANZHOU
Since yesterday had to throw me and bolt,
Today has hurt my heart even more.
The autumn wildgeese have a long wind for escort
As I face them from this villa, drinking my wine.
The bones of great writers are your brushes, in the School of Heaven,
And I am a Lesser Xie growing up by your side.
We both are exalted to distant thought,
Aspiring to the sky and the bright moon.
But since water still flows, though we cut it with our swords,
And sorrows return, though we drown them with wine,
Since the world can in no way answer our craving,
I will loosen my hair tomorrow and take to a fishingboat.
057
Seven-character-ancient-verse
Cen Can
A SONG OF RUNNING-HORSE RIVER IN FAREWELL
TO GENERAL FENG OF THE WESTERN EXPEDITION
Look how swift to the snowy sea races Running-Horse River! --
And sand, up from the desert, flies yellow into heaven.
This Ninth-month night is blowing cold at Wheel Tower,
And valleys, like peck measures, fill with the broken boulders
That downward, headlong, follow the wind.
...In spite of grey grasses, Tartar horses are plump;
West of the Hill of Gold, smoke and dust gather.
O General of the Chinese troops, start your campaign!
Keep your iron armour on all night long,
Send your soldiers forward with a clattering of weapons!
...While the sharp wind's point cuts the face like a knife,
And snowy sweat steams on the horses' backs,
Freezing a pattern of five-flower coins,
Your challenge from camp, from an inkstand of ice,
Has chilled the barbarian chieftain's heart.
You will have no more need of an actual battle! --
We await the news of victory, here at the western pass!
058
Seven-character-ancient-verse
Cen Can
A SONG OF WHEEL TOWER IN FAREWELL TO GENERAL
FENG OF THE WESTERN EXPEDITION
On Wheel Tower parapets night-bugles are blowing,
Though the flag at the northern end hangs limp.
Scouts, in the darkness, are passing Quli,
Where, west of the Hill of Gold, the Tartar chieftain has halted
We can see, from the look-out, the dust and black smoke
Where Chinese troops are camping, north of Wheel Tower.
...Our flags now beckon the General farther westWith bugles in the dawn he rouses his Grand Army;
Drums like a tempest pound on four sides
And the Yin Mountains shake with the shouts of ten thousand;
Clouds and the war-wind whirl up in a point
Over fields where grass-roots will tighten around white bones;
In the Dagger River mist, through a biting wind,
Horseshoes, at the Sand Mouth line, break on icy boulders.
...Our General endures every pain, every hardship,
Commanded to settle the dust along the border.
We have read, in the Green Books, tales of old daysBut here we behold a living man, mightier than the dead.
059
Seven-character-ancient-verse
Cen Can
A SONG OF WHITE SNOW IN FAREWELL
TO FIELD-CLERK WU GOING HOME
The north wind rolls the white grasses and breaks them;
And the Eighth-month snow across the Tartar sky
Is like a spring gale, come up in the night,
Blowing open the petals of ten thousand peartrees.
It enters the pearl blinds, it wets the silk curtains;
A fur coat feels cold, a cotton mat flimsy;
Bows become rigid, can hardly be drawn
And the metal of armour congeals on the men;
The sand-sea deepens with fathomless ice,
And darkness masses its endless clouds;
But we drink to our guest bound home from camp,
And play him barbarian lutes, guitars, harps;
Till at dusk, when the drifts are crushing our tents
And our frozen red flags cannot flutter in the wind,
We watch him through Wheel-Tower Gate going eastward.
Into the snow-mounds of Heaven-Peak Road....
And then he disappears at the turn of the pass,
Leaving behind him only hoof-prints.
060
Seven-character-ancient-verse
Du Fu
A DRAWING OF A HORSE BY GENERAL CAO
AT SECRETARY WEI FENG'S HOUSE
Throughout this dynasty no one had painted horses
Like the master-spirit, Prince Jiangdu --
And then to General Cao through his thirty years of fame
The world's gaze turned, for royal steeds.
He painted the late Emperor's luminous white horse.
For ten days the thunder flew over Dragon Lake,
And a pink-agate plate was sent him from the palaceThe talk of the court-ladies, the marvel of all eyes.
The General danced, receiving it in his honoured home
After this rare gift, followed rapidly fine silks
From many of the nobles, requesting that his art
Lend a new lustre to their screens.
...First came the curly-maned horse of Emperor Taizong,
Then, for the Guos, a lion-spotted horse....
But now in this painting I see two horses,
A sobering sight for whosoever knew them.
They are war- horses. Either could face ten thousand.
They make the white silk stretch away into a vast desert.
And the seven others with them are almost as noble
Mist and snow are moving across a cold sky,
And hoofs are cleaving snow-drifts under great treesWith here a group of officers and there a group of servants.
See how these nine horses all vie with one anotherThe high clear glance, the deep firm breath.
...Who understands distinction? Who really cares for art?
You, Wei Feng, have followed Cao; Zhidun preceded him.
...I remember when the late Emperor came toward his Summer Palace,
The procession, in green-feathered rows, swept from the eastern sky --
Thirty thousand horses, prancing, galloping,
Fashioned, every one of them, like the horses in this picture....
But now the Imperial Ghost receives secret jade from the River God,
For the Emperor hunts crocodiles no longer by the streams.
Where you see his Great Gold Tomb, you may hear among the pines
A bird grieving in the wind that the Emperor's horses are gone.
061
Seven-character-ancient-verse
Du Fu
A SONG OF A PAINTING TO GENERAL CAO
O General, descended from Wei's Emperor Wu,
You are nobler now than when a noble....
Conquerors and their valour perish,
But masters of beauty live forever.
...With your brush-work learned from Lady Wei
And second only to Wang Xizhi's,
Faithful to your art, you know no age,
Letting wealth and fame drift by like clouds.
...In the years of Kaiyuan you were much with the Emperor,
Accompanied him often to the Court of the South Wind.
When the spirit left great statesmen, on walls of the Hall of Fame
The point of your brush preserved their living faces.
You crowned all the premiers with coronets of office;
You fitted all commanders with arrows at their girdles;
You made the founders of this dynasty, with every hair alive,
Seem to be just back from the fierceness of a battle.
...The late Emperor had a horse, known as Jade Flower,
Whom artists had copied in various poses.
They led him one day to the red marble stairs
With his eyes toward the palace in the deepening air.
Then, General, commanded to proceed with your work,
You centred all your being on a piece of silk.
And later, when your dragon-horse, born of the sky,
Had banished earthly horses for ten thousand generations,
There was one Jade Flower standing on the dais
And another by the steps, and they marvelled at each other....
The Emperor rewarded you with smiles and with gifts,
While officers and men of the stud hung about and stared.
...Han Gan, your follower, has likewise grown proficient
At representing horses in all their attitudes;
But picturing the flesh, he fails to draw the boneSo that even the finest are deprived of their spirit.
You, beyond the mere skill, used your art divinelyAnd expressed, not only horses, but the life of a good man....
Yet here you are, wandering in a world of disorder
And sketching from time to time some petty passerby
People note your case with the whites of their eyes.
There's nobody purer, there's nobody poorer.
...Read in the records, from earliest times,
How hard it is to be a great artist.
062
Seven-character-ancient-verse
Du Fu
A LETTER TO CENSOR HAN
I am sad. My thoughts are in Youzhou.
I would hurry there-but I am sick in bed.
...Beauty would be facing me across the autumn waters.
Oh, to wash my feet in Lake Dongting and see at its eight corners
Wildgeese flying high, sun and moon both white,
Green maples changing to red in the frosty sky,
Angels bound for the Capital of Heaven, near the North Star,
Riding, some of them phrenixes, and others unicorns,
With banners of hibiscus and with melodies of mist,
Their shadows dancing upside-down in the southern rivers,
Till the Queen of the Stars, drowsy with her nectar,
Would forget the winged men on either side of her!
...From the Wizard of the Red Pine this word has come for me:
That after his earlier follower he has now a new disciple
Who, formerly at the capital as Emperor Liu's adviser,
In spite of great successes, never could be happy.
...What are a country's rise and fall?
Can flesh-pots be as fragrant as mountain fruit?....
I grieve that he is lost far away in the south.
May the star of long life accord him its blessing!
...O purity, to seize you from beyond the autumn waters
And to place you as an offering in the Court of Imperial Jade.
063
Seven-character-ancient-verse
Du Fu
A SONG OF AN OLD CYPRESS
Beside the Temple of the Great Premier stands an ancient cypress
With a trunk of green bronze and a root of stone.
The girth of its white bark would be the reach of forty men
And its tip of kingfish-blue is two thousand feet in heaven.
Dating from the days of a great ruler's great statesman,
Their very tree is loved now and honoured by the people.
Clouds come to it from far away, from the Wu cliffs,
And the cold moon glistens on its peak of snow.
...East of the Silk Pavilion yesterday I found
The ancient ruler and wise statesman both worshipped in one temple,
Whose tree, with curious branches, ages the whole landscape
In spite of the fresh colours of the windows and the doors.
And so firm is the deep root, so established underground,
That its lone lofty boughs can dare the weight of winds,
Its only protection the Heavenly Power,
Its only endurance the art of its Creator.
Though oxen sway ten thousand heads, they cannot move a mountain.
...When beams are required to restore a great house,
Though a tree writes no memorial, yet people understand
That not unless they fell it can use be made of it....
Its bitter heart may be tenanted now by black and white ants,
But its odorous leaves were once the nest of phoenixes and pheasants.
...Let wise and hopeful men harbour no complaint.
The greater the timber, the tougher it is to use.
064
Seven-character-ancient-verse
Du Fu
A SONG OF DAGGER-DANCING TO A GIRL-PUPIL
OF LADY GONGSUN
On the 19th of the Tenth-month in the second year of Dali, I saw, in
the
house of the Kueifu official Yuante, a girl named Li from Lingying
dancing with a dagger. I admired her skill and asked who was her
teacher. She named Lady Gongsun. I remembered that in the third year of
Kaiyuan at Yancheng, when I was a little boy, I saw Lady Gongsun dance.
She was the only one in the Imperial Theatre who could dance with this
weapon. Now she is aged and unknown, and even her pupil has passed the
heyday of beauty. I wrote this poem to express my wistfulness. The work
of Zhang Xu of the Wu district, that great master of grassy writing,
was
improved by his having been present when Lady Gongsun danced in the Yeh
district. From this may be judged the art of Gongsun.
There lived years ago the beautiful Gongsun,
Who, dancing with her dagger, drew from all four quarters
An audience like mountains lost among themselves.
Heaven and earth moved back and forth, following her motions,
Which were bright as when the Archer shot the nine suns down the sky
And rapid as angels before the wings of dragons.
She began like a thunderbolt, venting its anger,
And ended like the shining calm of rivers and the sea....
But vanished are those red lips and those pearly sleeves;
And none but this one pupil bears the perfume of her fame,
This beauty from Lingying, at the Town of the White God,
Dancing still and singing in the old blithe way.
And while we reply to each other's questions,
We sigh together, saddened by changes that have come.
There were eight thousand ladies in the late Emperor's court,
But none could dance the dagger-dance like Lady Gongsun.
...Fifty years have passed, like the turning of a palm;
Wind and dust, filling the world, obscure the Imperial House.
Instead of the Pear-Garden Players, who have blown by like a mist,
There are one or two girl-musicians now-trying to charm the cold Sun.
There are man-size trees by the Emperor's Golden Tomb
I seem to hear dead grasses rattling on the cliffs of Qutang.
...The song is done, the slow string and quick pipe have ceased.
At the height of joy, sorrow comes with the eastern moon rising.
And I, a poor old man, not knowing where to go,
Must harden my feet on the lone hills, toward sickness and despair.
065
Seven-character-ancient-verse
Yuan Jie
A DRINKING SONG AT STONE-FISH LAKE
I have used grain from the public fields, for distilling wine. After my
office hours I have the wine loaded on a boat and then I seat my
friends
on the bank of the lake. The little wine-boats come to each of us and
supply us with wine. We seem to be drinking on Pa Islet in Lake
Dongting. And I write this poem.
Stone-Fish Lake is like Lake Dongting --
When the top of Zun is green and the summer tide is rising.
...With the mountain for a table, and the lake a fount of wine,
The tipplers all are settled along the sandy shore.
Though a stiff wind for days has roughened the water,
Wine-boats constantly arrive....
I have a long-necked gourd and, happy on Ba Island,
I am pouring a drink in every direction doing away with care.
066
Seven-character-ancient-verse
Han Yu
MOUNTAIN-STONES
Rough were the mountain-stones, and the path very narrow;
And when I reached the temple, bats were in the dusk.
I climbed to the hall, sat on the steps, and drank the rain- washed air
Among the round gardenia-pods and huge bananaleaves.
On the old wall, said the priest, were Buddhas finely painted,
And he brought a light and showed me, and I called them wonderful
He spread the bed, dusted the mats, and made my supper ready,
And, though the food was coarse, it satisfied my hunger.
At midnight, while I lay there not hearing even an insect,
The mountain moon with her pure light entered my door....
At dawn I left the mountain and, alone, lost my way:
In and out, up and down, while a heavy mist
Made brook and mountain green and purple, brightening everything.
I am passing sometimes pines and oaks, which ten men could not girdle,
I am treading pebbles barefoot in swift-running water --
Its ripples purify my ear, while a soft wind blows my garments....
These are the things which, in themselves, make life happy.
Why should we be hemmed about and hampered with people?
O chosen pupils, far behind me in my own country,
What if I spent my old age here and never went back home?
067
Seven-character-ancient-verse
Han Yu
ON THE FESTIVAL OF THE MOON
TO SUB-OFFICIAL ZHANG
The fine clouds have opened and the River of Stars is gone,
A clear wind blows across the sky, and the moon widens its wave,
The sand is smooth, the water still, no sound and no shadow,
As I offer you a cup of wine, asking you to sing.
But so sad is this song of yours and so bitter your voice
That before I finish listening my tears have become a rain:
"Where Lake Dongting is joined to the sky by the lofty Nine-Doubt
Mountain,
Dragons, crocodiles, rise and sink, apes, flying foxes, whimper....
At a ten to one risk of death, I have reached my official post,
Where lonely I live and hushed, as though I were in hiding.
I leave my bed, afraid of snakes; I eat, fearing poisons;
The air of the lake is putrid, breathing its evil odours....
Yesterday, by the district office, the great drum was announcing
The crowning of an emperor, a change in the realm.
The edict granting pardons runs three hundred miles a day,
All those who were to die have had their sentences commuted,
The unseated are promoted and exiles are recalled,
Corruptions are abolished, clean officers appointed.
My superior sent my name in but the governor would not listen
And has only transferred me to this barbaric place.
My rank is very low and useless to refer to;
They might punish me with lashes in the dust of the street.
Most of my fellow exiles are now returning home --
A journey which, to me, is a heaven beyond climbing."
...Stop your song, I beg you, and listen to mine,
A song that is utterly different from yours:
"Tonight is the loveliest moon of the year.
All else is with fate, not ours to control;
But, refusing this wine, may we choose more tomorrow?"
068
Seven-character-quatrain
Han Yu
STOPPING AT A TEMPLE ON HENG MOUNTAIN I
INSCRIBE THIS POEM IN THE GATE-TOWER
The five Holy Mountains have the rank of the Three Dukes.
The other four make a ring, with the Song Mountain midmost.
To this one, in the fire-ruled south, where evil signs are rife,
Heaven gave divine power, ordaining it a peer.
All the clouds and hazes are hidden in its girdle;
And its forehead is beholden only by a few.
...I came here in autumn, during the rainy season,
When the sky was overcast and the clear wind gone.
I quieted my mind and prayed, hoping for an answer;
For assuredly righteous thinking reaches to high heaven.
And soon all the mountain-peaks were showing me their faces;
I looked up at a pinnacle that held the clean blue sky:
The wide Purple-Canopy joined the Celestial Column;
The Stone Granary leapt, while the Fire God stood still.
Moved by this token, I dismounted to offer thanks.
A long path of pine and cypress led to the temple.
Its white walls and purple pillars shone, and the vivid colour
Of gods and devils filled the place with patterns of red and blue.
I climbed the steps and, bending down to sacrifice, besought
That my pure heart might be welcome, in spite of my humble offering.
The old priest professed to know the judgment of the God:
He was polite and reverent, making many bows.
He handed me divinity-cups, he showed me how to use them
And told me that my fortune was the very best of all.
Though exiled to a barbarous land, mine is a happy life.
Plain food and plain clothes are all I ever wanted.
To be prince, duke, premier, general, was never my desire;
And if the God would bless me, what better could he grant than this ? -
-
At night I lie down to sleep in the top of a high tower;
While moon and stars glimmer through the darkness of the clouds....
Apes call, a bell sounds. And ready for dawn
I see arise, far in the east the cold bright sun.
069
Seven-character-ancient-verse
Han Yu
A POEM ON THE STONE DRUMS
Chang handed me this tracing, from the stone drums,
Beseeching me to write a poem on the stone drums.
Du Fu has gone. Li Bai is dead.
What can my poor talent do for the stone drums?
...When the Zhou power waned and China was bubbling,
Emperor Xuan, up in wrath, waved his holy spear:
And opened his Great Audience, receiving all the tributes
Of kings and lords who came to him with a tune of clanging weapons.
They held a hunt in Qiyang and proved their marksmanship:
Fallen birds and animals were strewn three thousand miles.
And the exploit was recorded, to inform new generations....
Cut out of jutting cliffs, these drums made of stoneOn which poets and artisans, all of the first order,
Had indited and chiselled-were set in the deep mountains
To be washed by rain, baked by sun, burned by wildfire,
Eyed by evil spirits; and protected by the gods.
...Where can he have found the tracing on this paper? --
True to the original, not altered by a hair,
The meaning deep, the phrases cryptic, difficult to read.
And the style of the characters neither square nor tadpole.
Time has not yet vanquished the beauty of these letters --
Looking like sharp daggers that pierce live crocodiles,
Like phoenix-mates dancing, like angels hovering down,
Like trees of jade and coral with interlocking branches,
Like golden cord and iron chain tied together tight,
Like incense-tripods flung in the sea, like dragons mounting heaven.
Historians, gathering ancient poems, forgot to gather these,
To make the two Books of Musical Song more colourful and striking;
Confucius journeyed in the west, but not to the Qin Kingdom,
He chose our planet and our stars but missed the sun and moon
I who am fond of antiquity, was born too late
And, thinking of these wonderful things, cannot hold back my tears....
I remember, when I was awarded my highest degree,
During the first year of Yuanho,
How a friend of mine, then at the western camp,
Offered to assist me in removing these old relics.
I bathed and changed, then made my plea to the college president
And urged on him the rareness of these most precious things.
They could be wrapped in rugs, be packed and sent in boxes
And carried on only a few camels: ten stone drums
To grace the Imperial Temple like the Incense-Pot of Gao --
Or their lustre and their value would increase a hundredfold,
If the monarch would present them to the university,
Where students could study them and doubtless decipher them,
And multitudes, attracted to the capital of culture
Prom all corners of the Empire, would be quick to gather.
We could scour the moss, pick out the dirt, restore the original
surface,
And lodge them in a fitting and secure place for ever,
Covered by a massive building with wide eaves
Where nothing more might happen to them as it had before.
...But government officials grow fixed in their ways
And never will initiate beyond old precedent;
So herd- boys strike the drums for fire, cows polish horns on them,
With no one to handle them reverentially.
Still ageing and decaying, soon they may be effaced.
Six years I have sighed for them, chanting toward the west....
The familiar script of Wang Xizhi, beautiful though it was,
Could be had, several pages, just for a few white geese,
But now, eight dynasties after the Zhou, and all the wars over,
Why should there be nobody caring for these drums?
The Empire is at peace, the government free.
Poets again are honoured and Confucians and Mencians....
Oh, how may this petition be carried to the throne?
It needs indeed an eloquent flow, like a cataractBut, alas, my voice has broken, in my song of the stone drums,
To a sound of supplication choked with its own tears.
070
Seven-character-ancient-verse
Liu Zongyuan
AN OLD FISHERMAN
An old fisherman spent the night here, under the western cliff;
He dipped up water from the pure Hsiang and made a bamboo fire;
And then, at sunrise, he went his way through the cloven mist,
With only the creak of his paddle left, in the greenness of mountain
and
river.
...I turn and see the waves moving as from heaven,
And clouds above the cliffs coming idly, one by one.
071
Seven-character-ancient-verse
Bai Juyi
A SONG OF UNENDING SORROW
China's Emperor, craving beauty that might shake an empire,
Was on the throne for many years, searching, never finding,
Till a little child of the Yang clan, hardly even grown,
Bred in an inner chamber, with no one knowing her,
But with graces granted by heaven and not to be concealed,
At last one day was chosen for the imperial household.
If she but turned her head and smiled, there were cast a hundred spells,
And the powder and paint of the Six Palaces faded into nothing.
...It was early spring. They bathed her in the FlowerPure Pool,
Which warmed and smoothed the creamy-tinted crystal of her skin,
And, because of her languor, a maid was lifting her
When first the Emperor noticed her and chose her for his bride.
The cloud of her hair, petal of her cheek, gold ripples of her crown
when she moved,
Were sheltered on spring evenings by warm hibiscus curtains;
But nights of spring were short and the sun arose too soon,
And the Emperor, from that time forth, forsook his early hearings
And lavished all his time on her with feasts and revelry,
His mistress of the spring, his despot of the night.
There were other ladies in his court, three thousand of rare beauty,
But his favours to three thousand were concentered in one body.
By the time she was dressed in her Golden Chamber, it would be almost
evening;
And when tables were cleared in the Tower of Jade, she would loiter,
slow with wine.
Her sisters and her brothers all were given titles;
And, because she so illumined and glorified her clan,
She brought to every father, every mother through the empire,
Happiness when a girl was born rather than a boy.
...High rose Li Palace, entering blue clouds,
And far and wide the breezes carried magical notes
Of soft song and slow dance, of string and bamboo music.
The Emperor's eyes could never gaze on her enoughTill war-drums, booming from Yuyang, shocked the whole earth
And broke the tunes of The Rainbow Skirt and the Feathered Coat.
The Forbidden City, the nine-tiered palace, loomed in the dust
From thousands of horses and chariots headed southwest.
The imperial flag opened the way, now moving and now pausing- -
But thirty miles from the capital, beyond the western gate,
The men of the army stopped, not one of them would stir
Till under their horses' hoofs they might trample those motheyebrows....
Flowery hairpins fell to the ground, no one picked them up,
And a green and white jade hair-tassel and a yellowgold hair- bird.
The Emperor could not save her, he could only cover his face.
And later when he turned to look, the place of blood and tears
Was hidden in a yellow dust blown by a cold wind.
... At the cleft of the Dagger-Tower Trail they crisscrossed through a
cloud-line
Under Omei Mountain. The last few came.
Flags and banners lost their colour in the fading sunlight....
But as waters of Shu are always green and its mountains always blue,
So changeless was His Majesty's love and deeper than the days.
He stared at the desolate moon from his temporary palace.
He heard bell-notes in the evening rain, cutting at his breast.
And when heaven and earth resumed their round and the dragon car faced
home,
The Emperor clung to the spot and would not turn away
From the soil along the Mawei slope, under which was buried
That memory, that anguish. Where was her jade-white face?
Ruler and lords, when eyes would meet, wept upon their coats
As they rode, with loose rein, slowly eastward, back to the capital.
...The pools, the gardens, the palace, all were just as before,
The Lake Taiye hibiscus, the Weiyang Palace willows;
But a petal was like her face and a willow-leaf her eyebrow --
And what could he do but cry whenever he looked at them?
...Peach-trees and plum-trees blossomed, in the winds of spring;
Lakka-foliage fell to the ground, after autumn rains;
The Western and Southern Palaces were littered with late grasses,
And the steps were mounded with red leaves that no one swept away.
Her Pear-Garden Players became white-haired
And the eunuchs thin-eyebrowed in her Court of PepperTrees;
Over the throne flew fire-flies, while he brooded in the twilight.
He would lengthen the lamp-wick to its end and still could never sleep.
Bell and drum would slowly toll the dragging nighthours
And the River of Stars grow sharp in the sky, just before dawn,
And the porcelain mandarin-ducks on the roof grow thick with morning
frost
And his covers of kingfisher-blue feel lonelier and colder
With the distance between life and death year after year;
And yet no beloved spirit ever visited his dreams.
...At Lingqiong lived a Taoist priest who was a guest of heaven,
Able to summon spirits by his concentrated mind.
And people were so moved by the Emperor's constant brooding
That they besought the Taoist priest to see if he could find her.
He opened his way in space and clove the ether like lightning,
Up to heaven, under the earth, looking everywhere.
Above, he searched the Green Void, below, the Yellow Spring;
But he failed, in either place, to find the one he looked for.
And then he heard accounts of an enchanted isle at sea,
A part of the intangible and incorporeal world,
With pavilions and fine towers in the five-coloured air,
And of exquisite immortals moving to and fro,
And of one among them-whom they called The Ever TrueWith a face of snow and flowers resembling hers he sought.
So he went to the West Hall's gate of gold and knocked at the jasper
door
And asked a girl, called Morsel-of-Jade, to tell The Doubly- Perfect.
And the lady, at news of an envoy from the Emperor of China,
Was startled out of dreams in her nine-flowered, canopy.
She pushed aside her pillow, dressed, shook away sleep,
And opened the pearly shade and then the silver screen.
Her cloudy hair-dress hung on one side because of her great haste,
And her flower-cap was loose when she came along the terrace,
While a light wind filled her cloak and fluttered with her motion
As though she danced The Rainbow Skirt and the Feathered Coat.
And the tear-drops drifting down her sad white face
Were like a rain in spring on the blossom of the pear.
But love glowed deep within her eyes when she bade him thank her liege,
Whose form and voice had been strange to her ever since their parting -
-
Since happiness had ended at the Court of the Bright Sun,
And moons and dawns had become long in Fairy-Mountain Palace.
But when she turned her face and looked down toward the earth
And tried to see the capital, there were only fog and dust.
So she took out, with emotion, the pledges he had given
And, through his envoy, sent him back a shell box and gold hairpin,
But kept one branch of the hairpin and one side of the box,
Breaking the gold of the hairpin, breaking the shell of the box;
"Our souls belong together," she said, " like this gold and this shell
--
Somewhere, sometime, on earth or in heaven, we shall surely
And she sent him, by his messenger, a sentence reminding him
Of vows which had been known only to their two hearts:
"On the seventh day of the Seventh-month, in the Palace of Long Life,
We told each other secretly in the quiet midnight world
That we wished to fly in heaven, two birds with the wings of one,
And to grow together on the earth, two branches of one tree."
Earth endures, heaven endures; some time both shall end,
While this unending sorrow goes on and on for ever.
072
Seven-character-ancient-verse
Bai Chuyi
THE SONG OF A GUITAR
In the tenth year of Yuanhe I was banished and demoted to be assistant
official in Jiujiang. In the summer of the next year I was seeing a
friend leave Penpu and heard in the midnight from a neighbouring boat a
guitar played in the manner of the capital. Upon inquiry, I found that
the player had formerly been a dancing-girl there and in her maturity
had been married to a merchant. I invited her to my boat to have her
play for us. She told me her story, heyday and then unhappiness. Since
my departure from the capital I had not felt sad; but that night, after
I left her, I began to realize my banishment. And I wrote this long
poem
-- six hundred and twelve characters.
I was bidding a guest farewell, at night on the Xunyang River,
Where maple-leaves and full-grown rushes rustled in the autumn.
I, the host, had dismounted, my guest had boarded his boat,
And we raised our cups and wished to drink-but, alas, there was no
music.
For all we had drunk we felt no joy and were parting from each other,
When the river widened mysteriously toward the full moon --
We had heard a sudden sound, a guitar across the water.
Host forgot to turn back home, and guest to go his way.
We followed where the melody led and asked the player's name.
The sound broke off...then reluctantly she answered.
We moved our boat near hers, invited her to join us,
Summoned more wine and lanterns to recommence our banquet.
Yet we called and urged a thousand times before she started toward us,
Still hiding half her face from us behind her guitar.
...She turned the tuning-pegs and tested several strings;
We could feel what she was feeling, even before she played:
Each string a meditation, each note a deep thought,
As if she were telling us the ache of her whole life.
She knit her brows, flexed her fingers, then began her music,
Little by little letting her heart share everything with ours.
She brushed the strings, twisted them slow, swept them, plucked them --
First the air of The Rainbow Skirt, then The Six Little Ones.
The large strings hummed like rain,
The small strings whispered like a secret,
Hummed, whispered-and then were intermingled
Like a pouring of large and small pearls into a plate of jade.
We heard an oriole, liquid, hidden among flowers.
We heard a brook bitterly sob along a bank of sand...
By the checking of its cold touch, the very string seemed broken
As though it could not pass; and the notes, dying away
Into a depth of sorrow and concealment of lament,
Told even more in silence than they had told in sound....
A silver vase abruptly broke with a gush of water,
And out leapt armored horses and weapons that clashed and smote --
And, before she laid her pick down, she ended with one stroke,
And all four strings made one sound, as of rending silk
There was quiet in the east boat and quiet in the west,
And we saw the white autumnal moon enter the river's heart.
...When she had slowly placed the pick back among the strings,
She rose and smoothed her clothing and, formal, courteous,
Told us how she had spent her girlhood at the capital,
Living in her parents' house under the Mount of Toads,
And had mastered the guitar at the age of thirteen,
With her name recorded first in the class-roll of musicians,
Her art the admiration even of experts,
Her beauty the envy of all the leading dancers,
How noble youths of Wuling had lavishly competed
And numberless red rolls of silk been given for one song,
And silver combs with shell inlay been snapped by her rhythms,
And skirts the colour of blood been spoiled with stains of wine....
Season after season, joy had followed joy,
Autumn moons and spring winds had passed without her heeding,
Till first her brother left for the war, and then her aunt died,
And evenings went and evenings came, and her beauty faded --
With ever fewer chariots and horses at her door;
So that finally she gave herself as wife to a merchant
Who, prizing money first, careless how he left her,
Had gone, a month before, to Fuliang to buy tea.
And she had been tending an empty boat at the river's mouth,
No company but the bright moon and the cold water.
And sometimes in the deep of night she would dream of her triumphs
And be wakened from her dreams by the scalding of her tears.
Her very first guitar-note had started me sighing;
Now, having heard her story, I was sadder still.
"We are both unhappy -- to the sky's end.
We meet. We understand. What does acquaintance matter?
I came, a year ago, away from the capital
And am now a sick exile here in Jiujiang --
And so remote is Jiujiang that I have heard no music,
Neither string nor bamboo, for a whole year.
My quarters, near the River Town, are low and damp,
With bitter reeds and yellowed rushes all about the house.
And what is to be heard here, morning and evening? --
The bleeding cry of cuckoos, the whimpering of apes.
On flowery spring mornings and moonlit autumn nights
I have often taken wine up and drunk it all alone,
Of course there are the mountain songs and the village pipes,
But they are crude and-strident, and grate on my ears.
And tonight, when I heard you playing your guitar,
I felt as if my hearing were bright with fairymusic.
Do not leave us. Come, sit down. Play for us again.
And I will write a long song concerning a guitar."
...Moved by what I said, she stood there for a moment,
Then sat again to her strings-and they sounded even sadder,
Although the tunes were different from those she had played before....
The feasters, all listening, covered their faces.
But who of them all was crying the most?
This Jiujiang official. My blue sleeve was wet.
073
Seven-character-ancient-verse
Li Shangyin
THE HAN MONUMENT
The Son of Heaven in Yuanhe times was martial as a god
And might be likened only to the Emperors Xuan and Xi.
He took an oath to reassert the glory of the empire,
And tribute was brought to his palace from all four quarters.
Western Huai for fifty years had been a bandit country,
Wolves becoming lynxes, lynxes becoming bears.
They assailed the mountains and rivers, rising from the plains,
With their long spears and sharp lances aimed at the Sun.
But the Emperor had a wise premier, by the name of Du,
Who, guarded by spirits against assassination,
Hong at his girdle the seal of state, and accepted chief command,
While these savage winds were harrying the flags of the Ruler of Heaven.
Generals Suo, Wu, Gu, and Tong became his paws and claws;
Civil and military experts brought their writingbrushes,
And his recording adviser was wise and resolute.
A hundred and forty thousand soldiers, fighting like lions and tigers,
Captured the bandit chieftains for the Imperial Temple.
So complete a victory was a supreme event;
And the Emperor said: "To you, Du, should go the highest honour,
And your secretary, Yu, should write a record of it."
When Yu had bowed his head, he leapt and danced, saying:
"Historical writings on stone and metal are my especial art;
And, since I know the finest brush-work of the old masters,
My duty in this instance is more than merely official,
And I should be at fault if I modestly declined."
The Emperor, on hearing this, nodded many times.
And Yu retired and fasted and, in a narrow workroom,
His great brush thick with ink as with drops of rain,
Chose characters like those in the Canons of Yao and Xun,
And a style as in the ancient poems Qingmiao and Shengmin.
And soon the description was ready, on a sheet of paper.
In the morning he laid it, with a bow, on the purple stairs.
He memorialized the throne: "I, unworthy,
Have dared to record this exploit, for a monument."
The tablet was thirty feet high, the characters large as dippers;
It was set on a sacred tortoise, its columns flanked with ragons....
The phrases were strange with deep words that few could understand;
And jealousy entered and malice and reached the Emperor --
So that a rope a hundred feet long pulled the tablet down
And coarse sand and small stones ground away its face.
But literature endures, like the universal spirit,
And its breath becomes a part of the vitals of all men.
The Tang plate, the Confucian tripod, are eternal things,
Not because of their forms, but because of their inscriptions....
Sagacious is our sovereign and wise his minister,
And high their successes and prosperous their reign;
But unless it be recorded by a writing such as this,
How may they hope to rival the three and five good rulers?
I wish I could write ten thousand copies to read ten thousand times,
Till spittle ran from my lips and calluses hardened my fingers,
And still could hand them down, through seventy-two generations,
As corner-stones for Rooms of Great Deeds on the Sacred Mountains.
074
Folk-song-styled-verse
Gao Shi
A SONG OF THE YAN COUNTRY
In the sixth year of Kaiyuan, a friend returned from the border and
showed me the Yan Song. Moved by what he told me of the expedition, I
have written this poem to the same rhymes.
The northeastern border of China was dark with smoke and dust.
To repel the savage invaders, our generals, leaving their families,
Strode forth together, looking as heroes should look;
And having received from the Emperor his most gracious favour,
They marched to the beat of gong and drum through the Elm Pass.
They circled the Stone Tablet with a line of waving flags,
Till their captains over the Sea of Sand were twanging feathered orders.
The Tartar chieftain's hunting-fires glimmered along Wolf Mountain,
And heights and rivers were cold and bleak there at the outer border;
But soon the barbarians' horses were plunging through wind and rain.
Half of our men at the front were killed, but the other half are living,
And still at the camp beautiful girls dance for them and sing.
...As autumn ends in the grey sand, with the grasses all withered,
The few surviving watchers by the lonely wall at sunset,
Serving in a good cause, hold life and the foeman lightly.
And yet, for all that they have done, Elm Pass is still unsafe.
Still at the front, iron armour is worn and battered thin,
And here at home food-sticks are made of jade tears.
Still in this southern city young wives' hearts are breaking,
While soldiers at the northern border vainly look toward home.
The fury of the wind cuts our men's advance
In a place of death and blue void, with nothingness ahead.
Three times a day a cloud of slaughter rises over the camp;
And all night long the hour-drums shake their chilly booming,
Until white swords can be seen again, spattered with red blood.
...When death becomes a duty, who stops to think of fame?
Yet in speaking of the rigours of warfare on the desert
We name to this day Li, the great General, who lived long ago.
075
Folk-song-styled-verse
Li Qi
AN OLD WAR-SONG
Through the bright day up the mountain, we scan the sky for a war-torch;
At yellow dusk we water our horses in the boundaryriver;
And when the throb of watch-drums hangs in the sandy wind,
We hear the guitar of the Chinese Princess telling her endless woe....
Three thousand miles without a town, nothing but camps,
Till the heavy sky joins the wide desert in snow.
With their plaintive calls, barbarian wildgeese fly from night to night,
And children of the Tartars have many tears to shed;
But we hear that the Jade Pass is still under siege,
And soon we stake our lives upon our light warchariots.
Each year we bury in the desert bones unnumbered,
Yet we only watch for grape-vines coming into China.
076
Folk-song-styled-verse
Wang Wei
A SONG OF A GIRL FROM LOYANG
There's a girl from Loyang in the door across the street,
She looks fifteen, she may be a little older.
...While her master rides his rapid horse with jade bit an bridle,
Her handmaid brings her cod-fish in a golden plate.
On her painted pavilions, facing red towers,
Cornices are pink and green with peach-bloom and with willow,
Canopies of silk awn her seven-scented chair,
And rare fans shade her, home to her nine-flowered curtains.
Her lord, with rank and wealth and in the bud of life,
Exceeds in munificence the richest men of old.
He favours this girl of lowly birth, he has her taught to dance;
And he gives away his coral-trees to almost anyone.
The wind of dawn just stirs when his nine soft lights go out,
Those nine soft lights like petals in a flying chain of flowers.
Between dances she has barely time for singing over the songs;
No sooner is she dressed again than incense burns before her.
Those she knows in town are only the rich and the lavish,
And day and night she is visiting the hosts of the gayest mansions.
...Who notices the girl from Yue with a face of white jade,
Humble, poor, alone, by the river, washing silk?
077
Folk-song-styled-verse
Wang Wei
SONG OF AN OLD GENERAL
When he was a youth of fifteen or twenty,
He chased a wild horse, he caught him and rode him,
He shot the white-browed mountain tiger,
He defied the yellow-bristled Horseman of Ye.
Fighting single- handed for a thousand miles,
With his naked dagger he could hold a multitude.
...Granted that the troops of China were as swift as heaven's thunder
And that Tartar soldiers perished in pitfalls fanged with iron,
General Wei Qing's victory was only a thing of chance.
And General Li Guang's thwarted effort was his fate, not his fault.
Since this man's retirement he is looking old and worn:
Experience of the world has hastened his white hairs.
Though once his quick dart never missed the right eye of a bird,
Now knotted veins and tendons make his left arm like an osier.
He is sometimes at the road-side selling melons from his garden,
He is sometimes planting willows round his hermitage.
His lonely lane is shut away by a dense grove,
His vacant window looks upon the far cold mountains
But, if he prayed, the waters would come gushing for his men
And never would he wanton his cause away with wine.
...War-clouds are spreading, under the Helan Range;
Back and forth, day and night, go feathered messages;
In the three River Provinces, the governors call young men --
And five imperial edicts have summoned the old general.
So he dusts his iron coat and shines it like snowWaves his dagger from its jade hilt in a dance of starry steel.
He is ready with his strong northern bow to smite the Tartar chieftain
--
That never a foreign war-dress may affront the Emperor.
...There once was an aged Prefect, forgotten and far away,
Who still could manage triumph with a single stroke.
078
Folk-song-styled-verse
Wang Wei
A SONG OF PEACH-BLOSSOM RIVER
A fisherman is drifting, enjoying the spring mountains,
And the peach-trees on both banks lead him to an ancient source.
Watching the fresh-coloured trees, he never thinks of distance
Till he comes to the end of the blue stream and suddenly- strange men!
It's a cave-with a mouth so narrow that he has to crawl through;
But then it opens wide again on a broad and level path --
And far beyond he faces clouds crowning a reach of trees,
And thousands of houses shadowed round with flowers and bamboos....
Woodsmen tell him their names in the ancient speech of Han;
And clothes of the Qin Dynasty are worn by all these people
Living on the uplands, above the Wuling River,
On farms and in gardens that are like a world apart,
Their dwellings at peace under pines in the clear moon,
Until sunrise fills the low sky with crowing and barking.
...At news of a stranger the people all assemble,
And each of them invites him home and asks him where he was born.
Alleys and paths are cleared for him of petals in the morning,
And fishermen and farmers bring him their loads at dusk....
They had left the world long ago, they had come here seeking refuge;
They have lived like angels ever since, blessedly far away,
No one in the cave knowing anything outside,
Outsiders viewing only empty mountains and thick clouds.
...The fisherman, unaware of his great good fortune,
Begins to think of country, of home, of worldly ties,
Finds his way out of the cave again, past mountains and past rivers,
Intending some time to return, when he has told his kin.
He studies every step he takes, fixes it well in mind,
And forgets that cliffs and peaks may vary their appearance.
...It is certain that to enter through the deepness of the mountain,
A green river leads you, into a misty wood.
But now, with spring-floods everywhere and floating peachpetals --
Which is the way to go, to find that hidden source?
079
Folk-song-styled-verse
Li Bai
HARD ROADS IN SHU
Oh, but it is high and very dangerous!
Such travelling is harder than scaling the blue sky.
...Until two rulers of this region
Pushed their way through in the misty ages,
Forty-eight thousand years had passed
With nobody arriving across the Qin border.
And the Great White Mountain, westward, still has only a bird's path
Up to the summit of Emei Peak --
Which was broken once by an earthquake and there were brave men lost,
Just finishing the stone rungs of their ladder toward heaven.
...High, as on a tall flag, six dragons drive the sun,
While the river, far below, lashes its twisted course.
Such height would be hard going for even a yellow crane,
So pity the poor monkeys who have only paws to use.
The Mountain of Green Clay is formed of many circlesEach hundred steps, we have to turn nine turns among its mound --
Panting, we brush Orion and pass the Well Star,
Then, holding our chests with our hands and sinking to the ground with
a
groan,
We wonder if this westward trail will never have an end.
The formidable path ahead grows darker, darker still,
With nothing heard but the call of birds hemmed in by the ancient
forest,
Male birds smoothly wheeling, following the females;
And there come to us the melancholy voices of the cuckoos
Out on the empty mountain, under the lonely moon....
Such travelling is harder than scaling the blue sky.
Even to hear of it turns the cheek pale,
With the highest crag barely a foot below heaven.
Dry pines hang, head down, from the face of the cliffs,
And a thousand plunging cataracts outroar one another
And send through ten thousand valleys a thunder of spinning stones.
With all this danger upon danger,
Why do people come here who live at a safe distance?
...Though Dagger-Tower Pass be firm and grim,
And while one man guards it
Ten thousand cannot force it,
What if he be not loyal,
But a wolf toward his fellows?
...There are ravenous tigers to fear in the day
And venomous reptiles in the night
With their teeth and their fangs ready
To cut people down like hemp.
Though the City of Silk be delectable, I would rather turn home quickly.
Such travelling is harder than scaling the blue sky....
But I still face westward with a dreary moan.
080
Folk-song-styled-verse
Li Bai
ENDLESS YEARNING I
"I am endlessly yearning
To be in Changan.
...Insects hum of autumn by the gold brim of the well;
A thin frost glistens like little mirrors on my cold mat;
The high lantern flickers; and. deeper grows my longing.
I lift the shade and, with many a sigh, gaze upon the moon,
Single as a flower, centred from the clouds.
Above, I see the blueness and deepness of sky.
Below, I see the greenness and the restlessness of water....
Heaven is high, earth wide; bitter between them flies my sorrow.
Can I dream through the gateway, over the mountain?
Endless longing
Breaks my heart."
081
Folk-song-styled-verse
Li Bai
ENDLESS YEARNING II
"The sun has set, and a mist is in the flowers;
And the moon grows very white and people sad and sleepless.
A Zhao harp has just been laid mute on its phoenix holder,
And a Shu lute begins to sound its mandarin-duck strings....
Since nobody can bear to you the burden of my song,
Would that it might follow the spring wind to Yanran Mountain.
I think of you far away, beyond the blue sky,
And my eyes that once were sparkling
Are now a well of tears.
...Oh, if ever you should doubt this aching of my heart,
Here in my bright mirror come back and look at me!"
082
Folk-song-styled-verse
Li Bai
THE HARD ROAD
Pure wine costs, for the golden cup, ten thousand coppers a flagon,
And a jade plate of dainty food calls for a million coins.
I fling aside my food-sticks and cup, I cannot eat nor drink....
I pull out my dagger, I peer four ways in vain.
I would cross the Yellow River, but ice chokes the ferry;
I would climb the Taihang Mountains, but the sky is blind with snow....
I would sit and poise a fishing-pole, lazy by a brook --
But I suddenly dream of riding a boat, sailing for the sun....
Journeying is hard,
Journeying is hard.
There are many turnings --
Which am I to follow?....
I will mount a long wind some day and break the heavy waves
And set my cloudy sail straight and bridge the deep, deep sea.
083
Folk-song-styled-verse
Li Bai
HARD IS THE WAY OF THE WORLD II
The way is broad like the blue sky,
But no way out before my eye.
I am ashamed to follow those who have no guts,
Gambling on fighting cocks and dogs for pears and nuts.
Feng would go homeward way, having no fish to eat;
Zhou did not think to bow to noblemen was meet.
General Han was mocked in the market-place;
The brilliant scholar Jia was banished in disgrace.
Have you not heard of King of Yan in days gone by,
Who venerated talents and built Terrace high
On which he offered gold to gifted men
And stooped low and swept the floor to welcome them?
Grateful, Ju Xin and Yue Yi came then
And served him heart and soul, both full of stratagem.
The King's bones were now buried,
who would sweep the floor of the Gold Terrace any more?
Hard is the way.
Go back without delay!
084
Folk-song-styled-verse
Li Bai
HARD IS THE WAY OF THE WORLD III
Don't wash your ears on hearing something you dislike
Nor die of hunger like famous hermits on the Pike!
Living without a fame among the motley crowd,
Why should one be as lofty as the moon or cloud?
Of ancient talents who failed to retire, there's none
But came to tragic ending after glory's won.
The head of General Wu was hung o'er city gate;
In the river was drowned the poet laureate.
The highly talented scholar wished in vain
To preserve his life to hear the cry of the crane.
Minister Li regretted not to have retired
To hunt with falcon gray as he had long desired.
Have you not heard of Zhang Han who resigned, carefree,
To go home to eat his perch with high glee?
Enjoy a cup of wine while you're alive!
Do not care if your fame will not survive!
085
Folk-song-styled-verse
Li Bai
BRINGING IN THE WINE
See how the Yellow River's waters move out of heaven.
Entering the ocean, never to return.
See how lovely locks in bright mirrors in high chambers,
Though silken-black at morning, have changed by night to snow.
...Oh, let a man of spirit venture where he pleases
And never tip his golden cup empty toward the moon!
Since heaven gave the talent, let it be employed!
Spin a thousand pieces of silver, all of them come back!
Cook a sheep, kill a cow, whet the appetite,
And make me, of three hundred bowls, one long drink!
...To the old master, Cen,
And the young scholar, Danqiu,
Bring in the wine!
Let your cups never rest!
Let me sing you a song!
Let your ears attend!
What are bell and drum, rare dishes and treasure?
Let me be forever drunk and never come to reason!
Sober men of olden days and sages are forgotten,
And only the great drinkers are famous for all time.
...Prince Chen paid at a banquet in the Palace of Perfection
Ten thousand coins for a cask of wine, with many a laugh and quip.
Why say, my host, that your money is gone?
Go and buy wine and we'll drink it together!
My flower-dappled horse,
My furs worth a thousand,
Hand them to the boy to exchange for good wine,
And we'll drown away the woes of ten thousand generations!
086
Folk-song-styled-verse
Du Fu
A SONG OF WAR-CHARIOTS
The war-chariots rattle,
The war-horses whinny.
Each man of you has a bow and a quiver at his belt.
Father, mother, son, wife, stare at you going,
Till dust shall have buried the bridge beyond Changan.
They run with you, crying, they tug at your sleeves,
And the sound of their sorrow goes up to the clouds;
And every time a bystander asks you a question,
You can only say to him that you have to go.
...We remember others at fifteen sent north to guard the river
And at forty sent west to cultivate the campfarms.
The mayor wound their turbans for them when they started out.
With their turbaned hair white now, they are still at the border,
At the border where the blood of men spills like the sea --
And still the heart of Emperor Wu is beating for war.
...Do you know that, east of China's mountains, in two hundred
districts
And in thousands of villages, nothing grows but weeds,
And though strong women have bent to the ploughing,
East and west the furrows all are broken down?
...Men of China are able to face the stiffest battle,
But their officers drive them like chickens and dogs.
Whatever is asked of them,
Dare they complain?
For example, this winter
Held west of the gate,
Challenged for taxes,
How could they pay?
...We have learned that to have a son is bad luckIt is very much better to have a daughter
Who can marry and live in the house of a neighbour,
While under the sod we bury our boys.
...Go to the Blue Sea, look along the shore
At all the old white bones forsaken --
New ghosts are wailing there now with the old,
Loudest in the dark sky of a stormy day.
087
Folk-song-styled-verse
Du Fu
A SONG OF FAIR WOMEN
On the third day of the Third-month in the freshening weather
Many beauties take the air by the Changan waterfront,
Receptive, aloof, sweet-mannered, sincere,
With soft fine skin and well-balanced bone.
Their embroidered silk robes in the spring sun are gleaming --
With a mass of golden peacocks and silver unicorns.
And hanging far down from their temples
Are blue leaves of delicate kingfisher feathers.
And following behind them
Is a pearl-laden train, rhythmic with bearers.
Some of them are kindred to the Royal House --
The titled Princesses Guo and Qin.
Red camel-humps are brought them from jade broilers,
And sweet fish is ordered them on crystal trays.
Though their food-sticks of unicorn-horn are lifted languidly
And the finely wrought phoenix carving-knife is very little used,
Fleet horses from the Yellow Gate, stirring no dust,
Bring precious dishes constantly from the imperial kitchen.
...While a solemn sound of flutes and drums invokes gods and spirits,
Guests and courtiers gather, all of high rank;
And finally, riding slow, a dignified horseman
Dismounts at the pavilion on an embroidered rug.
In a snow of flying willow-cotton whitening the duckweed,
Bluebirds find their way with vermilion handkerchiefs --
But power can be as hot as flame and burn people's fingers.
Be wary of the Premier, watch for his frown.
088
Folk-song-styled-verse
Du Fu
A SONG OF SOBBING BY THE RIVER
I am only an old woodsman, whispering a sob,
As I steal like a spring-shadow down the Winding River.
...Since the palaces ashore are sealed by a thousand gates --
Fine willows, new rushes, for whom are you so green?
...I remember a cloud of flags that came from the South Garden,
And ten thousand colours, heightening one another,
And the Kingdom's first Lady, from the Palace of the Bright Sun,
Attendant on the Emperor in his royal chariot,
And the horsemen before them, each with bow and arrows,
And the snowy horses, champing at bits of yellow gold,
And an archer, breast skyward, shooting through the clouds
And felling with one dart a pair of flying birds.
...Where are those perfect eyes, where are those pearly teeth?
A blood-stained spirit has no home, has nowhere to return.
And clear Wei waters running east, through the cleft on Dagger- Tower
Trail,
Carry neither there nor here any news of her.
People, compassionate, are wishing with tears
That she were as eternal as the river and the flowers.
...Mounted Tartars, in the yellow twilight, cloud the town with dust.
I am fleeing south, but I linger-gazing northward toward the throne.
089
Folk-song-styled-verse
Du Fu
A SONG OF A PRINCE DEPOSED
Along the wall of the Capital a white-headed crow
Flies to the Gate where Autumn Enters and screams there in the night,
Then turns again and pecks among the roofs of a tall mansion
Whose lord, a mighty mandarin, has fled before the Tartars,
With his golden whip now broken, his nine war-horses dead
And his own flesh and bone scattered to the winds....
There's a rare ring of green coral underneath the vest
Of a Prince at a street-corner, bitterly sobbing,
Who has to give a false name to anyone who asks himJust a poor fellow, hoping for employment.
A hundred days' hiding in grasses and thorns
Show on his body from head to foot.
But, since their first Emperor, all with hooknoses,
These Dragons look different from ordinary men.
Wolves are in the palace now and Dragons are lost in the desert --
O Prince, be very careful of your most sacred person!
I dare not address you long, here by the open road,
Nor even to stand beside you for more than these few moments.
Last night with the spring-wind there came a smell of blood;
The old Capital is full of camels from the east.
Our northern warriors are sound enough of body and of hand --
Oh, why so brave in olden times and so craven now?
Our Emperor, we hear, has given his son the throne
And the southern border-chieftains are loyally inclined
And the Huamen and Limian tribes are gathering to avenge us.
But still be careful-keep yourself well hidden from the dagger.
Unhappy Prince, I beg you, be constantly on guard --
Till power blow to your aid from the Five Imperial Tombs.
090
Five-character-regular-verse
Tang Xunzong
I PASS THROUGH THE LU DUKEDOM
WITH A SIGH AND A SACRIFICE FOR CONFUCIUS
O Master, how did the world repay
Your life of long solicitude? --
The Lords of Zou have misprized your land,
And your home has been used as the palace of Lu....
You foretold that when phoenixes vanished, your fortunes too would end,
You knew that the captured unicorn would be a sign of the dose of your
teaching....
Can this sacrifice I watch, here between two temple pillars,
Be the selfsame omen of death you dreamed of long ago?
091
Five-character-regular-verse
Zhang Jiuling
LOOKING AT THE MOON
AND THINKING OF ONE FAR AWAY
The moon, grown full now over the sea,
Brightening the whole of heaven,
Brings to separated hearts
The long thoughtfulness of night....
It is no darker though I blow out my candle.
It is no warmer though I put on my coat.
So I leave my message with the moon
And turn to my bed, hoping for dreams.
092
Five-character-regular-verse
Wang Bo
FAREWELL TO VICE-PREFECT DU
SETTING OUT FOR HIS OFFICIAL POST IN SHU
By this wall that surrounds the three Qin districts,
Through a mist that makes five rivers one,
We bid each other a sad farewell,
We two officials going opposite ways....
And yet, while China holds our friendship,
And heaven remains our neighbourhood,
Why should you linger at the fork of the road,
Wiping your eyes like a heart-broken child?
093
Five-character-regular-verse
Lo Bingwang
A POLITICAL PRISONER LISTENING TO A CICADA
While the year sinks westward, I hear a cicada
Bid me to be resolute here in my cell,
Yet it needed the song of those black wings
To break a white-haired prisoner's heart....
His flight is heavy through the fog,
His pure voice drowns in the windy world.
Who knows if he be singing still? - -
Who listens any more to me?
094
Five-character-regular-verse
Du Shenyan
ON A WALK IN THE EARLY SPRING
HARMONIZING A POEM BY MY FRIEND LU
STATIONED AT CHANGZHOU
Only to wanderers can come
Ever new the shock of beauty,
Of white cloud and red cloud dawning from the sea,
Of spring in the wild-plum and river-willow....
I watch a yellow oriole dart in the warm air,
And a green water- plant reflected by the sun.
Suddenly an old song fills
My heart with home, my eyes with tears.
095
Five-character-regular-verse
Shen Quanqi
LINES
Against the City of the Yellow Dragon
Our troops were sent long years ago,
And girls here watch the same melancholy moon
That lights our Chinese warriors --
And young wives dream a dream of spring,
That last night their heroic husbands,
In a great attack, with flags and drums,
Captured the City of the Yellow Dragon.
096
Five-character-regular-verse
Song Zhiwen
INSCRIBED ON THE WALL OF AN INN
NORTH OF DAYU MOUNTAIN
They say that wildgeese, flying southward,
Here turn back, this very month....
Shall my own southward journey
Ever be retraced, I wonder?
...The river is pausing at ebb-tide,
And the woods are thick with clinging mist --
But tomorrow morning, over the mountain,
Dawn will be white with the plum-trees of home.
097
Five-character-regular-verse
Wang Wan
A MOORING UNDER NORTH FORT HILL
Under blue mountains we wound our way,
My boat and 1, along green water;
Until the banks at low tide widened,
With no wind stirring my lone sail.
...Night now yields to a sea of sun,
And the old year melts in freshets.
At last I can send my messengers --
Wildgeese, homing to Loyang.
098
Five-character-regular-verse
Chang Jian
A BUDDHIST RETREAT BEHIND BROKEN-MOUNTAIN TEMPLE
In the pure morning, near the old temple,
Where early sunlight points the tree-tops,
My path has wound, through a sheltered hollow
Of boughs and flowers, to a Buddhist retreat.
Here birds are alive with mountain-light,
And the mind of man touches peace in a pool,
And a thousand sounds are quieted
By the breathing of a temple-bell.
099
Five-character-regular-verse
Cen Can
A MESSAGE TO CENSOR Du Fu
AT HIS OFFICE IN THE LEFT COURT
Together we officials climbed vermilion steps,
To be parted by the purple walls....
Our procession, which entered the palace at dawn,
Leaves fragrant now at dusk with imperial incense.
...Grey heads may grieve for a fallen flower,
Or blue clouds envy a lilting bird;
But this reign is of heaven, nothing goes wrong,
There have been almost no petitions.
100
Five-character-regular-verse
Li Bai
A MESSAGE TO MENG HAORAN
Master, I hail you from my heart,
And your fame arisen to the skies....
Renouncing in ruddy youth the importance of hat and chariot,
You chose pine-trees and clouds; and now, whitehaired,
Drunk with the moon, a sage of dreams,
Flower- bewitched, you are deaf to the Emperor....
High mountain, how I long to reach you,
Breathing your sweetness even here!
101
Five-character-regular-verse
Li Bai
BIDDING A FRIEND FAREWELL AT JINGMEN FERRY
Sailing far off from Jingmen Ferry,
Soon you will be with people in the south,
Where the mountains end and the plains begin
And the river winds through wilderness....
The moon is lifted like a mirror,
Sea-clouds gleam like palaces,
And the water has brought you a touch of home
To draw your boat three hundred miles.
102
Five-character-regular-verse
Li Bai
A FAREWELL TO A FRIEND
With a blue line of mountains north of the wall,
And east of the city a white curve of water,
Here you must leave me and drift away
Like a loosened water-plant hundreds of miles....
I shall think of you in a floating cloud;
So in the sunset think of me.
...We wave our hands to say good-bye,
And my horse is neighing again and again.
103
Five-character-regular-verse
Li Bai
ON HEARING JUN THE BUDDHIST MONK
FROM SHU PLAY HIS LUTE
The monk from Shu with his green silk lute-case,
Walking west down Omei Mountain,
Has brought me by one touch of the strings
The breath of pines in a thousand valleys.
I hear him in the cleansing brook,
I hear him in the icy bells;
And I feel no change though the mountain darken
And cloudy autumn heaps the sky.
104
Five-character-regular-verse
Li Bai
THOUGHTS OF OLD TIME FROM A NIGHT-MOORING
UNDER MOUNT NIU-ZHU
This night to the west of the river-brim
There is not one cloud in the whole blue sky,
As I watch from my deck the autumn moon,
Vainly remembering old General Xie....
I have poems; I can read;
He heard others, but not mine.
...Tomorrow I shall hoist my sail,
With fallen maple-leaves behind me.
105
Five-character-regular-verse
Du Fu
ON A MOONLIGHT NIGHT
Far off in Fuzhou she is watching the moonlight,
Watching it alone from the window of her chamberFor our boy and girl, poor little babes,
Are too young to know where the Capital is.
Her cloudy hair is sweet with mist,
Her jade-white shoulder is cold in the moon.
...When shall we lie again, with no more tears,
Watching this bright light on our screen?
106
Five-character-regular-verse
Du Fu
A SPRING VIEW
Though a country be sundered, hills and rivers endure;
And spring comes green again to trees and grasses
Where petals have been shed like tears
And lonely birds have sung their grief.
...After the war-fires of three months,
One message from home is worth a ton of gold.
...I stroke my white hair. It has grown too thin
To hold the hairpins any more.
107
Five-character-regular-verse
Du Fu
A NIGHT-VIGIL IN THE LEFT COURT OF THE PALACE
Flowers are shadowed, the palace darkens,
Birds twitter by for a place to perch;
Heaven's ten thousand windows are twinkling,
And nine cloud-terraces are gleaming in the moonlight.
...While I wait for the golden lock to turn,
I hear jade pendants tinkling in the wind....
I have a petition to present in the morning,
All night I ask what time it is.
108
Five-character-regular-verse
Du Fu
TAKING LEAVE OF FRIENDS ON MY WAY TO HUAZHOU
In the second year of Zhide, I escaped from the capital through the
Gate
of Golden Light and went to Fengxiang. In the first year of Qianyuan, I
was appointed as official to Huazhou from my former post of Censor.
Friends and relatives gathered and saw me leave by the same gate. And I
wrote this poem.
This is the road by which I fled,
When the rebels had reached the west end of the city;
And terror, ever since, has clutched at my vitals
Lest some of my soul should never return.
...The court has come back now, filling the capital;
But the Emperor sends me away again.
Useless and old, I rein in my horse
For one last look at the thousand gates.
109
Five-character-regular-verse
Du Fu
REMEMBERING MY BROTHERS ON A MOONLIGHT NIGHT
A wanderer hears drums portending battle.
By the first call of autumn from a wildgoose at the border,
He knows that the dews tonight will be frost.
...How much brighter the moonlight is at home!
O my brothers, lost and scattered,
What is life to me without you?
Yet if missives in time of peace go wrong --
What can I hope for during war?
110
Five-character-regular-verse
Du Fu
TO LI BAI AT THE SKY SEND
A cold wind blows from the far sky....
What are you thinking of, old friend?
The wildgeese never answer me.
Rivers and lakes are flooded with rain.
...A poet should beware of prosperity,
Yet demons can haunt a wanderer.
Ask an unhappy ghost, throw poems to him
Where he drowned himself in the Milo River.
111
Five-character-regular-verse
Du Fu
A FAREWELL AT FENGJI STATION TO GENERAL YAN
This is where your comrade must leave you,
Turning at the foot of these purple mountains....
When shall we lift our cups again, I wonder,
As we did last night and walk in the moon?
The region is murmuring farewell
To one who was honoured through three reigns;
And back I go now to my river-village,
Into the final solitude.
112
Five-character-regular-verse
Du Fu
ON LEAVING THE TOMB OF PREMIER FANG
Having to travel back now from this far place,
I dismount beside your lonely tomb.
The ground where I stand is wet with my tears;
The sky is dark with broken clouds....
I who played chess with the great Premier
Am bringing to my lord the dagger he desired.
But I find only petals falling down,
I hear only linnets answering.
113
Five-character-regular-verse
Du Fu
A NIGHT ABROAD
A light wind is rippling at the grassy shore....
Through the night, to my motionless tall mast,
The stars lean down from open space,
And the moon comes running up the river.
...If only my art might bring me fame
And free my sick old age from office! --
Flitting, flitting, what am I like
But a sand-snipe in the wide, wide world!
114
Five-character-regular-verse
Du Fu
ON THE GATE-TOWER AT YOUZHOU
I had always heard of Lake Dongting --
And now at last I have climbed to this tower.
With Wu country to the east of me and Chu to the south,
I can see heaven and earth endlessly floating.
...But no word has reached me from kin or friends.
I am old and sick and alone with my boat.
North of this wall there are wars and mountains --
And here by the rail how can I help crying?
115
Five-character-regular-verse
Wang Wei
A MESSAGE FROM MY LODGE AT WANGCHUAN
TO PEI DI
The mountains are cold and blue now
And the autumn waters have run all day.
By my thatch door, leaning on my staff,
I listen to cicadas in the evening wind.
Sunset lingers at the ferry,
Supper-smoke floats up from the houses.
...Oh, when shall I pledge the great Hermit again
And sing a wild poem at Five Willows?
116
Five-character-regular-verse
Wang Wei
AN AUTUMN EVENING IN THE MOUNTAINS
After rain the empty mountain
Stands autumnal in the evening,
Moonlight in its groves of pine,
Stones of crystal in its brooks.
Bamboos whisper of washer-girls bound home,
Lotus-leaves yield before a fisher-boat --
And what does it matter that springtime has gone,
While you are here, O Prince of Friends?
117
Five-character-regular-verse
Wang Wei
BOUND HOME TO MOUNT SONG
The limpid river, past its bushes
Running slowly as my chariot,
Becomes a fellow voyager
Returning home with the evening birds.
A ruined city-wall overtops an old ferry,
Autumn sunset floods the peaks.
...Far away, beside Mount Song,
I shall close my door and be at peace.
118
Five-character-regular-verse
Wang Wei
MOUNT ZHONGNAN
Its massive height near the City of Heaven
Joins a thousand mountains to the corner of the sea.
Clouds, when I look back, close behind me,
Mists, when I enter them, are gone.
A central peak divides the wilds
And weather into many valleys.
...Needing a place to spend the night,
I call to a wood-cutter over the river.
119
Five-character-regular-verse
Wang Wei
ANSWERING VICE-PREFECT ZHANG
As the years go by, give me but peace,
Freedom from ten thousand matters.
I ask myself and always answer:
What can be better than coming home?
A wind from the pine-trees blows my sash,
And my lute is bright with the mountain moon.
You ask me about good and evil fortune?....
Hark, on the lake there's a fisherman singing!
120
Five-character-regular-verse
Wang Wei
TOWARD THE TEMPLE OF HEAPED FRAGRANCE
Not knowing the way to the Temple of Heaped Fragrance,
Under miles of mountain-cloud I have wandered
Through ancient woods without a human track;
But now on the height I hear a bell.
A rillet sings over winding rocks,
The sun is tempered by green pines....
And at twilight, close to an emptying pool,
Thought can conquer the Passion-Dragon.
121
Five-character-regular-verse
Wang Wei
A MESSAGE TO COMMISSIONER LI AT ZIZHOU
From ten thousand valleys the trees touch heaven;
On a thousand peaks cuckoos are calling;
And, after a night of mountain rain,
From each summit come hundreds of silken cascades.
...If girls are asked in tribute the fibre they weave,
Or farmers quarrel over taro fields,
Preside as wisely as Wenweng did....
Is fame to be only for the ancients?
122
Five-character-regular-verse
Wang Wei
A VIEW OF THE HAN RIVER
With its three southern branches reaching the Chu border,
And its nine streams touching the gateway of Jing,
This river runs beyond heaven and earth,
Where the colour of mountains both is and is not.
The dwellings of men seem floating along
On ripples of the distant sky --
These beautiful days here in Xiangyang
Make drunken my old mountain heart!
123
Five-character-regular-verse
Wang Wei
MY RETREAT AT MOUNT ZHONGNAN
My heart in middle age found the Way.
And I came to dwell at the foot of this mountain.
When the spirit moves, I wander alone
Amid beauty that is all for me....
I will walk till the water checks my path,
Then sit and watch the rising clouds --
And some day meet an old wood-cutter
And talk and laugh and never return.
124
Five-character-regular-verse
Meng Haoran
A MESSAGE FROM LAKE DONGTIN
TO PREMIER ZHANG
Here in the Eighth-month the waters of the lake
Are of a single air with heaven,
And a mist from the Yun and Meng valleys
Has beleaguered the city of Youzhou.
I should like to cross, but I can find no boat.
...How ashamed I am to be idler than you statesmen,
As I sit here and watch a fisherman casting
And emptily envy him his catch.
125
Five-character-regular-verse
Meng Haoran
ON CLIMBING YAN MOUNTAIN WITH FRIENDS
While worldly matters take their turn,
Ancient, modern, to and fro,
Rivers and mountains are changeless in their glory
And still to be witnessed from this trail.
Where a fisher-boat dips by a waterfall,
Where the air grows colder, deep in the valley,
The monument of Yang remains;
And we have wept, reading the words.
126
Five-character-regular-verse
Meng Haoran
AT A BANQUET IN THE HOUSE
OF THE TAOIST PRIEST MEI
In my bed among the woods, grieving that spring must end,
I lifted up the curtain on a pathway of flowers,
And a flashing bluebird bade me come
To the dwelling-place of the Red Pine Genie.
...What a flame for his golden crucible --
Peach-trees magical with buds ! --
And for holding boyhood in his face,
The rosy-flowing wine of clouds!
127
Five-character-regular-verse
Meng Haoran
ON RETURNING AT THE YEAR'S END TO
ZHONGNAN MOUNTAIN
I petition no more at the north palace-gate.
...To this tumble-down hut on Zhongnan Mountain
I was banished for my blunders, by a wise ruler.
I have been sick so long I see none of my friends.
My white hairs hasten my decline,
Like pale beams ending the old year.
Therefore I lie awake and ponder
On the pine-shadowed moonlight in my empty window.
128
Five-character-regular-verse
Meng Haoran
STOPPING AT A FRIEND'S FARM-HOUSE
Preparing me chicken and rice, old friend,
You entertain me at your farm.
We watch the green trees that circle your village
And the pale blue of outlying mountains.
We open your window over garden and field,
To talk mulberry and hemp with our cups in our hands.
...Wait till the Mountain Holiday --
I am coming again in chrysanthemum time.
129
Five-character-regular-verse
Meng Haoran
FROM QIN COUNTRY TO THE BUDDHIST PRIEST YUAN
How gladly I would seek a mountain
If I had enough means to live as a recluse!
For I turn at last from serving the State
To the Eastern Woods Temple and to you, my master.
...Like ashes of gold in a cinnamon-flame,
My youthful desires have been burnt with the yearsAnd tonight in the chilling sunset-wind
A cicada, singing, weighs on my heart.
130
Five-character-regular-verse
Meng Haoran
FROM A MOORING ON THE TONGLU
TO A FRIEND IN YANGZHOU
With monkeys whimpering on the shadowy mountain,
And the river rushing through the night,
And a wind in the leaves along both banks,
And the moon athwart my solitary sail,
I, a stranger in this inland district,
Homesick for my Yangzhou friends,
Send eastward two long streams of tears
To find the nearest touch of the sea.
131
Five-character-regular-verse
Meng Haoran
TAKING LEAVE OF WANG WEI
Slow and reluctant, I have waited
Day after day, till now I must go.
How sweet the road-side flowers might be
If they did not mean good-bye, old friend.
The Lords of the Realm are harsh to us
And men of affairs are not our kind.
I will turn back home, I will say no more,
I will close the gate of my old garden.
132
Five-character-regular-verse
Meng Haoran
MEMORIES IN EARLY WINTER
South go the wildgesse, for leaves are now falling,
And the water is cold with a wind from the north.
I remember my home; but the Xiang River's curves
Are walled by the clouds of this southern country.
I go forward. I weep till my tears are spent.
I see a sail in the far sky.
Where is the ferry? Will somebody tell me?
It's growing rough. It's growing dark.
133
Five-character-regular-verse
Liu Changqing
CLIMBING IN AUTUMN FOR A VIEW FROM THE TEMPLE
ON THE TERRACE OF GENERAL WU
So autumn breaks my homesick heart....
Few pilgrims venture climbing to a temple so wild,
Up from the lake, in the mountain clouds.
...Sunset clings in the old defences,
A stone gong shivers through the empty woods.
...Of the Southern Dynasty, what remains?
Nothing but the great River.
134
Five-character-regular-verse
Liu Chanqing
A FAREWELL TO GOVERNOR LI
ON HIS WAY HOME TO HANYANG
Sad wanderer, once you conquered the South,
Commanding a hundred thousand men;
Today, dismissed and dispossessed,
In your old age you remember glory.
Once, when you stood, three borders were still;
Your dagger was the scale of life.
Now, watching the great rivers, the Jiang and the Han,
On their ways in the evening, where do you go?
135
Five-character-regular-verse
Liu Changing
ON SEEING WANG LEAVE FOR THE SOUTH
Toward a mist upon the water
Still I wave my hand and sob,
For the flying bird is lost in space
Beyond a desolate green mountain....
But now the long river, the far lone sail,
five lakes, gleam like spring in the sunset;
And down an island white with duckweed
Comes the quiet of communion.
136
Five-character-regular-verse
Liu Changing
WHILE VISITING ON THE SOUTH STREAM
THE TAOIST PRIEST CHANG
Walking along a little path,
I find a footprint on the moss,
A while cloud low on the quiet lake,
Grasses that sweeten an idle door,
A pine grown greener with the rain,
A brook that comes from a mountain source --
And, mingling with Truth among the flowers,
I have forgotten what to say.
137
Five-character-regular-verse
Liu Changqing
NEW YEAR'S AT CHANGSHA
New Year's only deepens my longing,
Adds to the lonely tears of an exile
Who, growing old and still in harness,
Is left here by the homing spring....
Monkeys come down from the mountains to haunt me.
I bend like a willow, when it rains on the river.
I think of Jia Yi, who taught here and died hereAnd I wonder what my term shall be.
138
Five-character-regular-verse
Qian Qi
FAREWELL TO A JAPANESE BUDDHIST PRIEST
BOUND HOMEWARD
You were foreordained to find the source.
Now, tracing your way as in a dream
There where the sea floats up the sky,
You wane from the world in your fragile boat....
The water and the moon are as calm as your faith,
Fishes and dragons follow your chanting,
And the eye still watches beyond the horizon
The holy light of your single lantern.
139
Five-character-regular-verse
Qian Qi
FROM MY STUDY AT THE MOUTH OF THE VALLEY.
A MESSAGE TO CENSOR YANG
At a little grass-hut in the valley of the river,
Where a cloud seems born from a viney wall,
You will love the bamboos new with rain,
And mountains tender in the sunset.
Cranes drift early here to rest
And autumn flowers are slow to fade....
I have bidden my pupil to sweep the grassy path
For the coming of my friend.
140
Five-character-regular-verse
Wei Yingwu
A GREETING ON THE HUAI RIVER
TO MY OLD FRIENDS FROM LIANGCHUAN
We used to be companions on the Jiang and the Han,
And as often as we met, we were likely to be tipsy.
Since we left one another, floating apart like clouds,
Ten years have run like water-till at last we join again.
And we talk again and laugh again just as in earlier days,
Except that the hair on our heads is tinged now with grey.
Why not come along, then, all of us together,
And face the autumn mountains and sail along the Huai?
141
Five-character-regular-verse
Wei Yingwu
A FAREWELL IN THE EVENING RAIN TO LI CAO
Is it raining on the river all the way to Chu? -- -
The evening bell comes to us from Nanjing.
Your wet sail drags and is loath to be going
And shadowy birds are flying slow.
We cannot see the deep ocean-gate --
Only the boughs at Pukou, newly dripping.
Likewise, because of our great love,
There are threads of water on our faces.
142
Five-character-regular-verse
Han Hong
AN AUTUMN EVENING HARMONIZING
CHENG QIN'S POEM
While a cold wind is creeping under my mat,
And the city's naked wall grows pale with the autumn moon,
I see a lone wild-goose crossing the River of Stars,
And I hear, on stone in the night, thousands of washing mallets....
But, instead of wishing the season, as it goes,
To bear me also far away,
I have found your poem so beautiful
That I forget the homing birds.
143
Five-character-regular-verse
Liu Jixu
A POEM
On a road outreaching the white clouds,
By a spring outrunning the bluest river,
Petals come drifting on the wind
And the brook is sweet with them all the way.
My quiet gate is a mountain-trail,
And the willow-trees about my cottage
Sift on my sleeve, through the shadowy noon,
Distillations of the sun.
144
Five-character-regular-verse
Dai Shulun
CHANGING ON OLD FRIENDS IN A VILLAGE INN
While the autumn moon is pouring full
On a thousand night-levels among towns and villages,
There meet by chance, south of the river,
Dreaming doubters of a dream....
In the trees a wind has startled the birds,
And insects cower from cold in the grass;
But wayfarers at least have wine
And nothing to fear -- till the morning bell.
145
Five-character-regular-verse
Lu Lun
A FAREWELL TO LI DUAN
By my old gate, among yellow grasses,
Still we linger, sick at heart.
The way you must follow through cold clouds
Will lead you this evening into snow.
Your father died; you left home young;
Nobody knew of your misfortunes.
We cry, we say nothing. What can I wish you,
In this blowing wintry world?
146
Five-character-regular-verse
Li Yi
A BRIEF BUT HAPPY MEETING WITH MY BROTHER-IN LAW
"MEETING BY ACCIDENT, ONLY TO PART"
After these ten torn wearisome years
We have met again. We were both so changed
That hearing first your surname, I thought you a stranger --
Then hearing your given name, I remembered your young face....
All that has happened with the tides
We have told and told till the evening bell....
Tomorrow you journey to Youzhou,
Leaving autumn between us, peak after peak.
147
Five-character-regular-verse
Sikong Shu
A FAREWELL TO HAN SHEN AT THE YUNYANG INN
Long divided by river and sea,
For years we two have failed to meet --
And suddenly to find you seems like a dream....
With a catch in the throat, we ask how old we are.
...Our single lamp shines, through cold and wet,
On a bamboo- thicket sheathed in rain;
But forgetting the sadness that will come with tomorrow,
Let us share the comfort of this farewell wine.
148
Five-character-regular-verse
Sikong Shu
WHEN LU LUN MY COUSIN COMES FOR THE NIGHT
With no other neighbour but the quiet night,
Here I live in the same old cottage;
And as raindrops brighten yellow leaves,
The lamp illumines my white head....
Out of the world these many years,
I am ashamed to receive you here.
But you cannot come too often,
More than brother, lifelong friend.
149
Five-character-regular-verse
Sikiong Shu
TO A FRIEND BOUND NORTH
AFTER THE REBELLION
In dangerous times we two came south;
Now you go north in safety, without me.
But remember my head growing white among strangers,
When you look on the blue of the mountains of home.
...The moon goes down behind a ruined fort,
Leaving star-clusters above an old gate....
There are shivering birds and withering grasses,
Whichever way I turn my face.
150
Five-character-regular-verse
Liu Yuxi
IN THE TEMPLE OF THE FIRST KING OF SHU
Even in this world the spirit of a hero
Lives and reigns for thousands of years.
You were the firmest of the pot's three legs;
It was you who maintained the honour of the currency;
You chose a great premier to magnify your kingdom....
And yet you had a son so little like his father
That girls of your country were taken captive
To dance in the palace of the King of Wei.
151
Five-character-regular-verse
Zhang Ji
THINKING OF A FRIEND LOST
IN THE TIBETAN WAR
Last year you went with your troops to Tibet;
And when your men had vanished beyond the citywall,
News was cut off between the two worlds
As between the living and the dead.
No one has come upon a faithful horse guarding
A crumpled tent or torn flag, or any trace of you.
If only I knew, I might serve you in the temple,
Instead of these tears toward the far sky.
152
Five-character-regular-verse
Bai Juyi
GRASSES
Boundless grasses over the plain
Come and go with every season;
Wildfire never quite consumes them --
They are tall once more in the spring wind.
Sweet they press on the old high- road
And reach the crumbling city-gate....
O Prince of Friends, you are gone again....
I hear them sighing after you.
153
Five-character-regular-verse
Du Mu
A NIGHT AT A TAVERN
Solitary at the tavern,
I am shut in with loneliness and grief.
Under the cold lamp, I brood on the past;
I am kept awake by a lost wildgoose.
...Roused at dawn from a misty dream,
I read, a year late, news from home --
And I remember the moon like smoke on the river
And a fisher-boat moored there, under my door.
154
Five-character-regular-verse
Xu Hun
INSCRIBED IN THE INN AT TONG GATE
ON AN AUTUMN TRIP TO THE CAPITAL
Red leaves are fluttering down the twilight
Past this arbour where I take my wine;
Cloud-rifts are blowing toward Great Flower Mountain,
And a shower is crossing the Middle Ridge.
I can see trees colouring a distant wall.
I can hear the river seeking the sea,
As I the Imperial City tomorrow --
But I dream of woodsmen and fishermen.
155
Five-character-regular-verse
Xu Hun
EARLY AUTUMN
There's a harp in the midnight playing clear,
While the west wind rustles a green vine;
There's a low cloud touching the jade-white dew
And an early wildgoose in the River of Stars....
Night in the tall trees clings to dawn;
Light makes folds in the distant hills;
And here on the Huai, by one falling leaf,
I can feel a storm on Lake Dongting.
156
Five-character-regular-verse
Li Shangyin
A CICADA
Pure of heart and therefore hungry,
All night long you have sung in vain --
Oh, this final broken indrawn breath
Among the green indifferent trees!
Yes, I have gone like a piece of driftwood,
I have let my garden fill with weeds....
I bless you for your true advice
To live as pure a life as yours.
157
Five-character-regular-verse
Li Shangyin
WIND AND RAIN
I ponder on the poem of The Precious Dagger.
My road has wound through many years.
...Now yellow leaves are shaken with a gale;
Yet piping and fiddling keep the Blue Houses merry.
On the surface, I seem to be glad of new people;
But doomed to leave old friends behind me,
I cry out from my heart for Xinfeng wine
To melt away my thousand woes.
158
Five-character-regular-verse
Li Shangyin
FALLING PETALS
Gone is the guest from the Chamber of Rank,
And petals, confused in my little garden,
Zigzagging down my crooked path,
Escort like dancers the setting sun.
Oh, how can I bear to sweep them away?
To a sad-eyed watcher they never return.
Heart's fragrance is spent with the ending of spring
And nothing left but a tear-stained robe.
159
Five-character-regular-verse
Li Shangyin
THOUGHTS IN THE COLD
You are gone. The river is high at my door.
Cicadas are mute on dew-laden boughs.
This is a moment when thoughts enter deep.
I stand alone for a long while.
...The North Star is nearer to me now than spring,
And couriers from your southland never arrive --
Yet I doubt my dream on the far horizon
That you have found another friend.
160
Five-character-regular-verse
Li Shangyin
NORTH AMONG GREEN VINES
Where the sun has entered the western hills,
I look for a monk in his little straw hut;
But only the fallen leaves are at home,
And I turn through chilling levels of cloud
I hear a stone gong in the dusk,
I lean full-weight on my slender staff
How within this world, within this grain of dust,
Can there be any room for the passions of men?
161
Five-character-regular-verse
Wen Tingyun
TO A FRIEND BOUND EAST
The old fort brims with yellow leaves....
You insist upon forsaking this place where you have lived.
A high wind blows at Hanyang Ferry
And sunrise lights the summit of Yingmen....
Who will be left for me along the upper Yangzi
After your solitary skiff has entered the end of the sky?
I ask you over and over when we shall meet again,
While we soften with winecups this ache of farewell.
162
Five-character-regular-verse
Ma Dai
AN AUTUMN COTTAGE AT BASHANG
After the shower at Bashang,
I see an evening line of wildgeese,
The limp-hanging leaves of a foreign tree,
A lantern's cold gleam, lonely in the night,
An empty garden, white with dew,
The ruined wall of a neighbouring monastery.
...I have taken my ease here long enough.
What am I waiting for, I wonder.
163
Five-character-regular-verse
Ma Dai
THOUGHTS OF OLD TIME
ON THE CHU RIVER
A cold light shines on the gathering dew,
As sunset fades beyond the southern mountains;
Trees echo with monkeys on the banks of Lake Dongting,
Where somebody is moving in an orchid-wood boat.
Marsh-lands are swollen wide with the moon,
While torrents are bent to the mountains' will;
And the vanished Queens of the Clouds leave me
Sad with autumn all night long.
164
Five-character-regular-verse
Zhang Qiao
ON THE BORDER
Though a bugle breaks the crystal air of autumn,
Soldiers, in the look-out, watch at ease today
The spring wind blowing across green graves
And the pale sun setting beyond Liangzhou.
For now, on grey plains done with war,
The border is open to travel again;
And Tartars can no more choose than rivers:
They are running, all of them, toward the south.
165
Five-character-regular-verse
Cui Tu
ON NEW YEAR'S EVE
Farther and farther from the three Ba Roads,
I have come three thousand miles, anxious and watchful,
Through pale snow-patches in the jagged nightmountains --
A stranger with a lonely lantern shaken in the wind.
...Separation from my kin
Binds me closer to my servants --
Yet how I dread, so far adrift,
New Year's Day, tomorrow morning!
166
Five-character-regular-verse
Cui Tu
A SOLITARY WILDGOOSE
Line after line has flown back over the border.
Where are you headed all by yourself?
In the evening rain you call to them --
And slowly you alight on an icy pond.
The low wet clouds move faster than you
Along the wall toward the cold moon.
...If they caught you in a net or with a shot,
Would it be worse than flying alone?
167
Five-character-regular-verse
Du Xunhe
A SIGH IN THE SPRING PALACE
Knowing beauty my misfortune,
I face my mirror with a sigh.
To please a fastidious emperor,
How shall I array myself?....
Birds flock and sing when the wind is warm,
Flower-shadows climb when the sun is high --
And year after year girls in the south
Are picking hibiscus, dreaming of love!
168
Five-character-regular-verse
Wei Zhuang
A NIGHT THOUGHT ON TERRACE TOWER
Far through the night a harp is sighing
With a sadness of wind and rain in the strings....
There's a solitary lantern, a bugle-call --
And beyond Terrace Tower down goes the moon.
...Fragrant grasses have changed and faded
While still I have been hoping that my old friend would come....
There are no more messengers I can send him,
Now that the wildgeese have turned south.
169
Five-character-regular-verse
Seng Jiaoran
NOT FINDING LU HONGXIAN AT HOME
To find you, moved beyond the city,
A wide path led me, by mulberry and hemp,
To a new-set hedge of chrysanthemums --
Not yet blooming although autumn had come.
...I knocked; no answer, not even a dog.
I waited to ask your western neighbour;
But he told me that daily you climb the mountain,
Never returning until sunset.
170
Seven-character-regular-verse
Cui Hao
THE YELLOW CRANE TERRACE
Where long ago a yellow crane bore a sage to heaven,
Nothing is left now but the Yellow Crane Terrace.
The yellow crane never revisited earth,
And white clouds are flying without him for ever.
...Every tree in Hanyang becomes clear in the water,
And Parrot Island is a nest of sweet grasses;
But I look toward home, and twilight grows dark
With a mist of grief on the river waves.
171
Seven-character-regular-verse
Cui Hao
PASSING THROUGH HUAYIN
Lords of the capital, sharp, unearthly,
The Great Flower's three points pierce through heaven.
Clouds are parting above the Temple of the Warring Emperor,
Rain dries on the mountain, on the Giant's Palm.
Ranges and rivers are the strength of this western gate,
Whence roads and trails lead downward into China.
...O pilgrim of fame, O seeker of profit,
Why not remain here and lengthen your days?
172
Five-character-regular-verse
Zu Yong
LOOKING TOWARD AN INNER GATE
OF THE GREAT WALL
My heart sank when I headed north from Yan Country
To the camps of China echoing ith bugle and drum.
...In an endless cold light of massive snow,
Tall flags on three borders rise up like a dawn.
War-torches invade the barbarian moonlight,
Mountain-clouds like chairmen bear the Great Wall from the sea.
...Though no youthful clerk meant to be a great general,
I throw aside my writing-brush --
Like the student who tossed off cap for a lariat,
I challenge what may come.
173
Seven-character-regular-verse
Li Qi
A FAREWELL TO WEI WAN
The travellers' parting-song sounds in the dawn.
Last night a first frost came over the river;
And the crying of the wildgeese grieves my sad heart
Bounded by a gloom of cloudy mountains....
Here in the Gate City, day will flush cold
And washing-flails quicken by the gardens at twilight --
How long shall the capital content you,
Where the months and the years so vainly go by?
174
Seven-character-regular-verse
Cui Shu
A CLIMB ON THE MOUNTAIN HOLIDAY
TO THE TERRACE WHENCE ONE SEES THE MAGICIAN
A POEM SENT TO VICE-PREFECT LU
The Han Emperor Wen bequeathed us this terrace
Which I climb to watch the coming dawn.
Cloudy peaks run northward in the three Jin districts,
And rains are blowing westward through the two Ling valleys.
...Who knows but me about the Guard at the Gate,
Or where the Magician of the River Bank is,
Or how to find that magistrate, that poet,
Who was as fond as I am of chrysanthemums and winecups?
175
Seven-character-regular-verse
Li Bai
ON CLIMBING IN NANJING TO THE TERRACE
OF PHOENIXES
Phoenixes that played here once, so that the place was named for them,
Have abandoned it now to this desolate river;
The paths of Wu Palace are crooked with weeds;
The garments of Qin are ancient dust.
...Like this green horizon halving the Three Peaks,
Like this Island of White Egrets dividing the river,
A cloud has arisen between the Light of Heaven and me,
To hide his city from my melancholy heart.
176
Seven-character-regular-verse
Gao Shi
TO VICE-PREFECTS LI AND WANG DEGRADED AND
TRANSFERRED TO XIAZHONG AND CHANGSHA
What are you thinking as we part from one another,
Pulling in our horses for the stirrup-cups?
Do these tear-streaks mean Wu Valley monkeys all weeping,
Or wildgeese returning with news from Heng Mountain?....
On the river between green maples an autumn sail grows dim,
There are only a few old trees by the wall of the White God City....
But the year is bound to freshen us with a dew of heavenly favour --
Take heart, we shall soon be together again!
177
Seven-character-regular-verse
Cen Can
AN EARLY AUDIENCE AT THE PALACE OF LIGHT
HARMONIZING SECRETARY JIA ZHI'S POEM
Cock-crow, the Purple Road cold in the dawn;
Linnet songs, court roofs tinted with April;
At the Golden Gate morning bell, countless doors open,
And up the jade steps float a thousand officials
With flowery scabbards.... Stars have gone down;
Willows are brushing the dew from the flags --
And, alone on the Lake of the Phoenix, a guest
Is chanting too well The Song of Bright Spring.
178
Seven-character-regular-verse
Wang Wei
AN EARLY AUDIENCE AT THE PALACE OF LIGHT
HARMONIZING SECRETARY JIA ZHI POEM
The red-capped Cock-Man has just announced morning;
The Keeper of the Robes brings Jade-Cloud Furs;
Heaven's nine doors reveal the palace and its courtyards;
And the coats of many countries bow to the Pearl Crown.
Sunshine has entered the giants' carven palms;
Incense wreathes the Dragon Robe:
The audience adjourns-and the five-coloured edict
Sets girdle-beads clinking toward the Lake of the Phoenix.
179
Seven-character-regular-verse
Wang Wei
LOOKING DOWN IN A SPRING-RAIN ON THE COURSE
FROM FAIRY-MOUNTAIN PALACE TO THE PAVILION OF
INCREASE HARMONIZING THE EMPEROR'S POEM
Round a turn of the Qin Fortress winds the Wei River,
And Yellow Mountain foot-hills enclose the Court of China;
Past the South Gate willows comes the Car of Many Bells
On the upper Palace-Garden Road-a solid length of blossom;
A Forbidden City roof holds two phoenixes in cloud;
The foliage of spring shelters multitudes from rain;
And now, when the heavens are propitious for action,
Here is our Emperor ready-no wasteful wanderer.
180
Seven-character-regular-verse
Wang Wei
IN MY LODGE AT WANG CHUAN
AFTER A LONG RAIN
The woods have stored the rain, and slow comes the smoke
As rice is cooked on faggots and carried to the fields;
Over the quiet marsh-land flies a white egret,
And mango-birds are singing in the full summer trees....
I have learned to watch in peace the mountain morningglories,
To eat split dewy sunflower-seeds under a bough of pine,
To yield the post of honour to any boor at all....
Why should I frighten sea gulls, even with a thought?
181
Seven-character-regular-verse
Wang Wei
HARMONIZING A POEM BY PALACE-ATTENDANT GUO
High beyond the thick wall a tower shines with sunset
Where peach and plum are blooming and the willowcotton flies.
You have heard in your office the court-bell of twilight;
Birds find perches, officials head for home.
Your morning-jade will tinkle as you thread the golden palace;
You will bring the word of Heaven from the closing gates at night.
And I should serve there with you; but being full of years,
I have taken off official robes and am resting from my troubles.
182
Seven-character-regular-verse
Du Fu
THE TEMPLE OF THE PREMIER OF SHU
Where is the temple of the famous Premier? --
In a deep pine grove near the City of Silk,
With the green grass of spring colouring the steps,
And birds chirping happily under the leaves.
...The third summons weighted him with affairs of state
And to two generations he gave his true heart,
But before he could conquer, he was dead;
And heroes have wept on their coats ever since.
183
Seven-character-regular-verse
Du Fu
A HEARTY WELCOME TO VICE-PREFECT CUI
North of me, south of me, spring is in flood,
Day after day I have seen only gulls....
My path is full of petals -- I have swept it for no others.
My thatch gate has been closed -- but opens now for you.
It's a long way to the market, I can offer you little --
Yet here in my cottage there is old wine for our cups.
Shall we summon my elderly neighbour to join us,
Call him through the fence, and pour the jar dry?
184
Seven-character-regular-verse
Du Fu
A VIEW OF THE WILDERNESS
Snow is white on the westward mountains and on three fortified towns,
And waters in this southern lake flash on a long bridge.
But wind and dust from sea to sea bar me from my brothers;
And I cannot help crying, I am so far away.
I have nothing to expect now but the ills of old age.
I am of less use to my country than a grain of dust.
I ride out to the edge of town. I watch on the horizon,
Day after day, the chaos of the world.
185
Seven-character-regular-verse
Du Fu
BOTH SIDES OF THE YELLOW RIVER
RECAPTURED BY THE IMPERIAL ARMY
News at this far western station! The north has been recaptured!
At first I cannot check the tears from pouring on my coat --
Where is my wife? Where are my sons?
Yet crazily sure of finding them, I pack my books and poems- -
And loud my song and deep my drink
On the green spring-day that starts me home,
Back from this mountain, past another mountain,
Up from the south, north again-to my own town!
186
Seven-character-regular-verse
Du Fu
A LONG CLIMB
In a sharp gale from the wide sky apes are whimpering,
Birds are flying homeward over the clear lake and white sand,
Leaves are dropping down like the spray of a waterfall,
While I watch the long river always rolling on.
I have come three thousand miles away. Sad now with autumn
And with my hundred years of woe, I climb this height alone.
Ill fortune has laid a bitter frost on my temples,
Heart-ache and weariness are a thick dust in my wine.
187
Seven-character-regular-verse
Du Fu
FROM AN UPPER STORY
Flowers, as high as my window, hurt the heart of a wanderer
For I see, from this high vantage, sadness everywhere.
The Silken River, bright with spring, floats between earth and heaven
Like a line of cloud by the Jade Peak, between ancient days and now.
...Though the State is established for a while as firm as the North
Star
And bandits dare not venture from the western hills,
Yet sorry in the twilight for the woes of a longvanished Emperor,
I am singing the song his Premier sang when still unestranged from the
mountain.
188
Seven-character-regular-verse
Du Fu
STAYING AT THE GENERAL'S HEADQUARTERS
The autumn night is clear and cold in the lakka-trees of this courtyard.
I am lying forlorn in the river-town. I watch my guttering candle.
I hear the lonely notes of a bugle sounding through the dark.
The moon is in mid-heaven, but there's no one to share it with me.
My messengers are scattered by whirls of rain and sand.
City-gates are closed to a traveller; mountains are walls in my way --
Yet, I who have borne ten years of pitiable existence,
Find here a perch, a little branch, and am safe for this one night.
189
Seven-character-regular-verse
Du Fu
NIGHT IN THE WATCH-TOWER
While winter daylight shortens in the elemental scale
And snow and frost whiten the cold-circling night,
Stark sounds the fifth-watch with a challenge of drum and bugle.
...The stars and the River of Heaven pulse over the three mountains;
I hear women in the distance, wailing after the battle;
I see barbarian fishermen and woodcutters in the dawn.
...Sleeping-Dragon, Plunging-Horse, are no generals now, they are dust
--
Hush for a moment, O tumult of the world.
190
Seven-character-regular-verse
Du Fu
POETIC THOUGHTS ON ANCIENT SITES I
Forlorn in the northeast among wind and dust,
Drifting in the southwest between heaven and earth,
Lingering for days and months in towers and terraces at the Three
Gorges,
Sharing clouds and mountains with the costumes of the Five Streams.
The barbarian serving the ruler in the end was unreliable.
The wandering poet lamenting the times had no chance to return.
Yu Xin throughout his life was most miserable,
In his waning years his poetry stirred the land of rivers and passes.
191
Seven-character-regular-verse
Du Fu
POETIC THOUGHTS ON ANCIENT SITES II
"Decay and decline": deep knowledge have I of Sung Yu's grief.
Romantic and refined, he too is my teacher.
Sadly looking across a thousand autumns, one shower of tears,
Melancholy in different epochs, not at the same time.
Among rivers and mountains his old abode -- empty his writings;
Deserted terrace of cloud and rain -- surely not just imagined in a
dream?
Utterly the palaces of Chu are all destroyed and ruined,
The fishermen pointing them out today are unsure.
192
Seven-character-regular-verse
Du Fu
THOUGHTS OF OLD TIME III
Ten thousand ranges and valleys approach the Jing Gate
And the village in which the Lady of Light was born and bred.
She went out from the purple palace into the desertland;
She has now become a green grave in the yellow dusk.
Her face ! Can you picture a wind of the spring?
Her spirit by moonlight returns with a tinkling
Song of the Tartars on her jade guitar,
Telling her eternal sorrow.
193
Seven-character-regular-verse
Du Fu
POETIC THOUGHTS ON ANCIENT SITES IV
The ruler of Shu had his eyes on Wu and progressed as far as the Three
Gorges.
In the year of his demise, too, he was in the Palace of Eternal Peace.
The blue-green banners can be imagined on the empty mountain,
The jade palace is a void in the deserted temple.
In the pines of the ancient shrine aquatic cranes nest;
At summer and winter festivals the comers are village elders.
The Martial Marquis's memorial shrine is ever nearby;
In union, sovereign and minister share the sacrifices together.
194
Seven-character-regular-verse
Du Fu
THOUGHTS OF OLD TIME V
Zhuge's prestige transcends the earth;
There is only reverence for his face;
Yet his will, among the Three Kingdoms at war,
Was only as one feather against a flaming sky.
He was brother of men like Yi and Lu
And in time would have surpassed the greatest of all statesmen.
Though he knew there was no hope for the House of Han,
Yet he wielded his mind for it, yielded his life.
195
Seven-character-regular-verse
Liu Changquing
ON LEAVING GUIJIANG AGAIN TO XUE AND LIU
Dare I, at my age, accept my summons,
Knowing of the world's ways only wine and song?....
Over the moon-edged river come wildgeese from the Tartars;
And the thinner the leaves along the Huai, the wider the southern
mountains....
I ought to be glad to take my old bones back to the capital,
But what am I good for in that world, with my few white hairs?....
As bent and decrepit as you are, I am ashamed to thank you,
When you caution me that I may encounter thunderbolts.
196
Seven-character-regular-verse
Liu Changqing
ON PASSING JIA YI'S HOUSE IN CHANGSHA
Here, where you spent your three years' exile,
To be mourned in Chu ten thousand years,
Can I trace your footprint in the autumn grass --
Or only slanting sunlight through the bleak woods?
If even good Emperor Wen was cold-hearted,
Could you hope that the dull river Xiang would understand you,
These desolate waters, these taciturn mountains,
When you came, like me, so far away?
197
Seven-character-regular-verse
Liu Changqing
AN EVENING VIEW OF THE CITY OF YOUZHOU AFTER
COMING FROM HANKOU TO PARROT ISLAND A POEM SENT
TO MY FRIEND GOVERNOR YUAN
No ripples in the river, no mist on the islands,
Yet the landscape is blurred toward my friend in Chu....
Birds in the slanting sun cross Hankou,
And the autumn sky mingles with Lake Dongting.
...From a bleak mountain wall the cold tone of a bugle
Reminds me, moored by a ruined fort,
That Jia Yi's loyal plea to the House of Han
Banned him to Changsha, to be an exile.
198
Seven-character-regular-verse
Qian Qi
TO MY FRIEND AT THE CAPITAL SECRETARY PEI
Finches flash yellow through the Imperial Grove
Of the Forbidden City, pale with spring dawn;
Flowers muffle a bell in the Palace of Bliss
And rain has deepened the Dragon Lake willows;
But spring is no help to a man bewildered,
Who would be like a cloud upholding the Light of Heaven,
Yet whose poems, ten years refused, are shaming
These white hairs held by the petalled pin.
199
Seven-character-regular-verse
Wei Yingwu
TO MY FRIENDS LI DAN AND YUANXI
We met last among flowers, among flowers we parted,
And here, a year later, there are flowers again;
But, with ways of the world too strange to foretell,
Spring only brings me grief and fatigue.
I am sick, and I think of my home in the countryAshamed to take pay while so many are idle.
...In my western tower, because of your promise,
I have watched the full moons come and go.
200
Seven-character-regular-verse
Han Hong
INSCRIBED IN THE TEMPLE OF THE WANDERING GENIE
I face, high over this enchanted lodge, the Court of the Five Cities of
Heaven,
And I see a countryside blue and still, after the long rain.
The distant peaks and trees of Qin merge into twilight,
And Had Palace washing-stones make their autumnal echoes.
Thin pine-shadows brush the outdoor pulpit,
And grasses blow their fragrance into my little cave.
...Who need be craving a world beyond this one?
Here, among men, are the Purple Hills
201
Seven-character-regular-verse
Huangfu Ran
SPRING THOUGHTS
Finch-notes and swallow-notes tell the new year....
But so far are the Town of the Horse and the Dragon Mound
From this our house, from these walls and Han Gardens,
That the moon takes my heart to the Tartar sky.
I have woven in the frame endless words of my grieving....
Yet this petal-bough is smiling now on my lonely sleep.
Oh, ask General Dou when his flags will come home
And his triumph be carved on the rock of Yanran mountain!
202
Seven-character-regular-verse
Lu Lun
A NIGHT-MOORING AT WUCHANG
Far off in the clouds stand the walls of Hanyang,
Another day's journey for my lone sail....
Though a river-merchant ought to sleep in this calm weather,
I listen to the tide at night and voices of the boatmen.
...My thin hair grows wintry, like the triple Xiang streams,
Three thousand miles my heart goes, homesick with the moon;
But the war has left me nothing of my heritage --
And oh, the pang of hearing these drums along the river!
203
Seven-character-regular-verse
Liu Zongyuan
FROM THE CITY-TOWER OF LIUZHOU
TO MY FOUR FELLOW-OFFICIALS AT ZHANG,
DING, FENG, AND LIAN DISTRICTS
At this lofty tower where the town ends, wilderness begins;
And our longing has as far to go as the ocean or the sky....
Hibiscus-flowers by the moat heave in a sudden wind,
And vines along the wall are whipped with slanting rain.
Nothing to see for three hundred miles but a blur of woods and mountain
--
And the river's nine loops, twisting in our bowels....
This is where they have sent us, this land of tattooed people --
And not even letters, to keep us in touch with home.
204
Seven-character-regular-verse
Liu Yuxi
THOUGHTS OF OLD TIME AT WEST FORT MOUNTAIN
Since Wang Jun brought his towering ships down from Yizhou,
The royal ghost has pined in the city of Nanjing.
Ten thousand feet of iron chain were sunk here to the bottom --
And then came the flag of surrender on the Wall of Stone....
Cycles of change have moved into the past,
While still this mountain dignity has commanded the cold river;
And now comes the day of the Chinese world united,
And the old forts fill with ruin and with autumn reeds.
205
Seven-character-regular-verse
Yuan Zhen
AN ELEGY I
O youngest, best-loved daughter of Xie,
Who unluckily married this penniless scholar,
You patched my clothes from your own wicker basket,
And I coaxed off your hairpins of gold, to buy wine with;
For dinner we had to pick wild herbs --
And to use dry locust-leaves for our kindling.
...Today they are paying me a hundred thousand --
And all that I can bring to you is a temple sacrifice.
206
Seven-character-regular-verse
Yuan Zhen
AN ElEGY II
We joked, long ago, about one of us dying,
But suddenly, before my eyes, you are gone.
Almost all your clothes have been given away;
Your needlework is sealed, I dare not look at it....
I continue your bounty to our men and our maids --
Sometimes, in a dream, I bring you gifts.
...This is a sorrow that all mankind must know --
But not as those know it who have been poor together.
207
Seven-character-regular-verse
Yuan Zhen
AN ELEGY III
I sit here alone, mourning for us both.
How many years do I lack now of my threescore and ten?
There have been better men than I to whom heaven denied a son,
There was a poet better than I whose dead wife could not hear him.
What have I to hope for in the darkness of our tomb?
You and I had little faith in a meeting after deathYet my open eyes can see all night
That lifelong trouble of your brow.
208
Seven-character-regular-verse
Bai Juyi
TO MY BROTHERS AND SISTERS ADRIFT
IN TROUBLED TIMES THIS POEM OF THE MOON
Since the disorders in Henan and the famine in Guannei, my brothers and
sisters have been scattered. Looking at the moon, I express my thoughts
in this poem, which I send to my eldest brother at Fuliang, my seventh
brother at Yuqian, My fifteen brother at Wujiang and my younger
brothers
and sisters at Fuli and Xiagui.
My heritage lost through disorder and famine,
My brothers and sisters flung eastward and westward,
My fields and gardens wrecked by the war,
My own flesh and blood become scum of the street,
I moan to my shadow like a lone-wandering wildgoose,
I am torn from my root like a water-plant in autumn:
I gaze at the moon, and my tears run down
For hearts, in five places, all sick with one wish.
209
Seven-character-regular-verse
Li Shangyin
THE INLAID HARP
I wonder why my inlaid harp has fifty strings,
Each with its flower-like fret an interval of youth.
...The sage Chuangzi is day-dreaming, bewitched by butterflies,
The spring-heart of Emperor Wang is crying in a cuckoo,
Mermen weep their pearly tears down a moon-green sea,
Blue fields are breathing their jade to the sun....
And a moment that ought to have lasted for ever
Has come and gone before I knew.
210
Seven-character-regular-verse
Li Shangyin
TO ONE UNNAMED
The stars of last night and the wind of last night
Are west of the Painted Chamber and east of Cinnamon Hall.
...Though I have for my body no wings like those of the brightcoloured
phoenix,
Yet I feel the harmonious heart-beat of the Sacred Unicorn.
Across the spring-wine, while it warms me, I prompt you how to bet
Where, group by group, we are throwing dice in the light of a crimson
lamp;
Till the rolling of a drum, alas, calls me to my duties
And I mount my horse and ride away, like a water-plant cut adrift.
211
Seven-character-regular-verse
Li Shangyin
THE PALACE OF THE SUI EMPEROR
His Palace of Purple Spring has been taken by mist and cloud,
As he would have taken all Yangzhou to be his private domain
But for the seal of imperial jade being seized by the first Tang
Emperor,
He would have bounded with his silken sails the limits of the world.
Fire-flies are gone now, have left the weathered grasses,
But still among the weeping-willows crows perch at twilight.
...If he meets, there underground, the Later Chen Emperor,
Do you think that they will mention a Song of Courtyard Flowers?
212
Seven-character-regular-verse
Li Shangyin
TO ONE UNNAMED I
You said you would come, but you did not, and you left me with no other
trace
Than the moonlight on your tower at the fifth-watch bell.
I cry for you forever gone, I cannot waken yet,
I try to read your hurried note, I find the ink too pale.
...Blue burns your candle in its kingfisher-feather lantern
And a sweet breath steals from your hibiscus-broidered curtain.
But far beyond my reach is the Enchanted Mountain,
And you are on the other side, ten thousand peaks away.
213
Seven-character-regular-verse
Li Shangyin
TO ONE UNNAMED II
A misty rain comes blowing with a wind from the east,
And wheels faintly thunder beyond Hibiscus Pool.
...Round the golden-toad lock, incense is creeping;
The jade tiger tells, on its cord, of water being drawn
A great lady once, from behind a screen, favoured a poor youth;
A fairy queen brought a bridal mat once for the ease of a prince and
then vanished.
...Must human hearts blossom in spring, like all other flowers?
And of even this bright flame of love, shall there be only ashes?
214
Seven-character-regular-verse
Li Shangyin
IN THE CAMP OF THE SKETCHING BRUSH
Monkeys and birds are still alert for your orders
And winds and clouds eager to shield your fortress.
...You were master of the brush, and a sagacious general,
But your Emperor, defeated, rode the prison-cart.
You were abler than even the greatest Zhou statesmen,
Yet less fortunate than the two Shu generals who were killed in action.
And, though at your birth-place a temple has been built to you,
You never finished singing your Song of the Holy Mountain
215
Seven-character-regular-verse
Li Shangyin
TO ONE UNNAMED III
Time was long before I met her, but is longer since we parted,
And the east wind has arisen and a hundred flowers are gone,
And the silk-worms of spring will weave until they die
And every night the candles will weep their wicks away.
Mornings in her mirror she sees her hair-cloud changing,
Yet she dares the chill of moonlight with her evening song.
...It is not so very far to her Enchanted Mountain
O blue-birds, be listening!-Bring me what she says!
216
Seven-character-regular-verse
Li Shangyin
SPRING RAIN
I am lying in a white-lined coat while the spring approaches,
But am thinking only of the White Gate City where I cannot be.
...There are two red chambers fronting the cold, hidden by the rain,
And a lantern on a pearl screen swaying my lone heart homeward.
...The long road ahead will be full of new hardship,
With, late in the nights, brief intervals of dream.
Oh, to send you this message, this pair of jade earrings! --
I watch a lonely wildgoose in three thousand miles of cloud.
217
Seven-character-regular-verse
Li Shangyin
TO ONE UNNAMED IV
A faint phoenix-tail gauze, fragrant and doubled,
Lines your green canopy, closed for the night....
Will your shy face peer round a moon-shaped fan,
And your voice be heard hushing the rattle of my carriage?
It is quiet and quiet where your gold lamp dies,
How far can a pomegranate-blossom whisper?
...I will tether my horse to a river willow
And wait for the will of the southwest wind.
218
Seven-character-regular-verse
Li Shangyin
TO ONE UNNAMED V
There are many curtains in your care-free house,
Where rapture lasts the whole night long.
...What are the lives of angels but dreams
If they take no lovers into their rooms?
...Storms are ravishing the nut-horns,
Moon- dew sweetening cinnamon-leaves
I know well enough naught can come of this union,
Yet how it serves to ease my heart!
219
Seven-character-regular-verse
Wen Tingyun
NEAR THE LIZHOU FERRY
The sun has set in the water's clear void,
And little blue islands are one with the sky.
On the bank a horse neighs. A boat goes by.
People gather at a willow- clump and wait for the ferry.
Down by the sand-bushes sea-gulls are circling,
Over the wide river-lands flies an egret.
...Can you guess why I sail, like an ancient wise lover,
Through the misty Five Lakes, forgetting words?
220
Seven-character-regular-verse
Wen Tingyun
THE TEMPLE OF SU WU
Though our envoy, Su Wu, is gone, body and soul,
This temple survives, these trees endure....
Wildgeese through the clouds are still calling to the moon there
And hill-sheep unshepherded graze along the border.
...Returning, he found his country changed
Since with youthful cap and sword he had left it.
His bitter adventures had won him no title....
Autumn-waves endlessly sob in the river.
221
Seven-character-regular-verse
Xue Feng
A PALACE POEM
In twelve chambers the ladies, decked for the day,
Peer afar for their lord from their Fairy-View Lodge;
The golden toad guards the lock on the door-chain,
And the bronze-dragon water-clock drips through the morning
Till one of them, tilting a mirror, combs her cloud of hair
And chooses new scent and a change of silk raiment;
For she sees, between screen-panels, deep in the palace,
Eunuchs in court-dress preparing a bed.
222
Seven-character-regular-verse
Qin Taoyu
A POOR GIRL
Living under a thatch roof, never wearing fragrant silk,
She longs to arrange a marriage, but how could she dare?
Who would know her simple face the loveliest of them all
When we choose for worldliness, not for worth?
Her fingers embroider beyond compare,
But she cannot vie with painted brows;
And year after year she has sewn gold thread
On bridal robes for other girls.
223
Folk-song-styled-verse
Shen Quanqi
BEYOND SEEING
A girl of the Lu clan who lives in Golden-Wood Hall,
Where swallows perch in pairs on beams of tortoiseshell,
Hears the washing-mallets' cold beat shake the leaves down.
...The Liaoyang expedition will be gone ten years,
And messages are lost in the White Wolf River.
...Here in the City of the Red Phoenix autumn nights are long,
Where one who is heart-sick to see beyond seeing,
Sees only moonlight on the yellow-silk wave of her loom.
224
Five-character-quatrain
Wang Wei
DEER-PARK HERMITAGE
There seems to be no one on the empty mountain....
And yet I think I hear a voice,
Where sunlight, entering a grove,
Shines back to me from the green moss.
225
Five-character-quatrain
Wang Wei
IN A RETREAT AMONG BAMBOOS
Leaning alone in the close bamboos,
I am playing my lute and humming a song
Too softly for anyone to hear --
Except my comrade, the bright moon.
226
Five-character-quatrain
Wang Wei
A PARTING
Friend, I have watched you down the mountain
Till now in the dark I close my thatch door....
Grasses return again green in the spring,
But O my Prince of Friends, do you?
227
Five-character-quatrain
Wang Wei
ONE-HEARTED
When those red berries come in springtime,
Flushing on your southland branches,
Take home an armful, for my sake,
As a symbol of our love.
228
Five-character-quatrain
Wang Wei
LINES
You who have come from my old country,
Tell me what has happened there ! --
Was the plum, when you passed my silken window,
Opening its first cold blossom?
229
Five-character-quatrain
Pei Di
A FAREWELL TO CUI
Though you think to return to this maze of mountains,
Oh, let them brim your heart with wonder!....
Remember the fisherman from Wuling
Who had only a day in the Peach-Blossom Country.
230
Five-character-quatrain
Zu Young
ON SEEING THE SNOW-PEAK OF ZHONGNAN
See how Zhongnan Mountain soars
With its white top over floating clouds --
And a warm sky opening at the snow-line
While the town in the valley grows colder and colder.
231
Five-character-quatrain
Meng Haoran
A NIGHT-MOORING ON THE JIANDE RIVER
While my little boat moves on its mooring of mist,
And daylight wanes, old memories begin....
How wide the world was, how close the trees to heaven,
And how clear in the water the nearness of the moon!
232
Five-character-quatrain
Meng Haoran
A SPRING MORNING
I awake light-hearted this morning of spring,
Everywhere round me the singing of birds --
But now I remember the night, the storm,
And I wonder how many blossoms were broken.
233
Five-character-quatrain
Li Bai
IN THE QUIET NIGHT
So bright a gleam on the foot of my bed --
Could there have been a frost already?
Lifting myself to look, I found that it was moonlight.
Sinking back again, I thought suddenly of home.
234
Five-character-quatrain
Li Bai
A BITTER LOVE
How beautiful she looks, opening the pearly casement,
And how quiet she leans, and how troubled her brow is!
You may see the tears now, bright on her cheek,
But not the man she so bitterly loves.
235
Five-character-quatrain
Du Fu
THE EIGHT-SIDED FORTRESS
The Three Kingdoms, divided, have been bound by his greatness.
The Eight-Sided Fortress is founded on his fame;
Beside the changing river, it stands stony as his grief
That he never conquered the Kingdom of Wu.
236
Five-character-quatrain
Wang Zhihuan
AT HERON LODGE
Mountains cover the white sun,
And oceans drain the golden river;
But you widen your view three hundred miles
By going up one flight of stairs.
237
Five-character-quatrain
Liu Changqing
ON PARTING WITH THE BUDDHIST PILGRIM LING CHE
From the temple, deep in its tender bamboos,
Comes the low sound of an evening bell,
While the hat of a pilgrim carries the sunset
Farther and farther down the green mountain.
238
Five-character-quatrain
Liu Changqing
ON HEARING A LUTE-PLAYER
Your seven strings are like the voice
Of a cold wind in the pines,
Singing old beloved songs
Which no one cares for any more.
239
Five-character-quatrain
Liu Changqing
FAREWELL TO A BUDDHIST MONK
Can drifting clouds and white storks
Be tenants in this world of ours? --
Or you still live on Wuzhou Mountain,
Now that people are coming here?
240
Five-character-quatrain
Wei Yingwu
AN AUTUMN NIGHT MESSAGE TO QIU
As I walk in the cool of the autumn night,
Thinking of you, singing my poem,
I hear a mountain pine-cone fall....
You also seem to be awake.
241
Five-character-quatrain
Li Duan
ON HEARING HER PLAY THE HARP
Her hands of white jade by a window of snow
Are glimmering on a golden-fretted harp --
And to draw the quick eye of Chou Yu,
She touches a wrong note now and then.
242
Five-character-quatrain
Wang Jian
A BRIDE
On the third day, taking my place to cook,
Washing my hands to make the bridal soup,
I decide that not my mother-in-law
But my husband's young sister shall have the fiat taste.
243
Five-character-quatrain
Quan Deyu
THE JADE DRESSING-TABLE
Last night my girdle came undone,
And this morning a luck-beetle flew over my bed.
So here are my paints and here are my powders --
And a welcome for my yoke again.
244
Five-character-quatrain
Liu Zongyuan
RIVER-SNOW
A hundred mountains and no bird,
A thousand paths without a footprint;
A little boat, a bamboo cloak,
An old man fishing in the cold river-snow.
245
Five-character-quatrain
Yuan Zhen
THE SUMMER PALACE
In the faded old imperial palace,
Peonies are red, but no one comes to see them....
The ladies-in-waiting have grown white-haired
Debating the pomps of Emperor Xuanzong.
246
Five-character-quatrain
Bai Juyi
A SUGGESTION TO MY FRIEND LIU
There's a gleam of green in an old bottle,
There's a stir of red in the quiet stove,
There's a feeling of snow in the dusk outside --
What about a cup of wine inside?
247
Five-character-quatrain
Zhang Hu
SHE SINGS AN OLD SONG
A lady of the palace these twenty years,
She has lived here a thousand miles from her homeYet ask her for this song and, with the first few words of it,
See how she tries to hold back her tears.
248
Five-character-quatrain
Li Shangyin
THE LEYOU TOMBS
With twilight shadows in my heart
I have driven up among the Leyou Tombs
To see the sun, for all his glory,
Buried by the coming night.
249
Five-character-quatrain
Jia Dao
A NOTE LEFT FOR AN ABSENT ECLUSE
When I questioned your pupil, under a pine-tree,
"My teacher," he answered, " went for herbs,
But toward which corner of the mountain,
How can I tell, through all these clouds ?"
250
Five-character-quatrain
Li Pin
CROSSING THE HAN RIVER
Away from home, I was longing for news
Winter after winter, spring after spring.
Now, nearing my village, meeting people,
I dare not ask a single question.
251
Five-character-quatrain
Jin Changzu
A SPRING SIGH
Drive the orioles away,
All their music from the trees....
When she dreamed that she went to Liaoxi Camp
To join him there, they wakened her
252
Five-character-quatrain
Xibiren
GENERAL GE SHU
This constellation, with its seven high stars,
Is Ge Shu lifting his sword in the night:
And no more barbarians, nor their horses, nor cattle,
Dare ford the river boundary.
253
Folk-song-styled-verse
Cui Hao
A SONG OF CHANGGAN I
"Tell me, where do you live? --
Near here, by the fishing-pool?
Let's hold our boats together, let's see
If we belong in the same town."
254
Folk-song-styled-verse
Cui Hao
A SONG OF CHANGGAN II
"Yes, I live here, by the river;
I have sailed on it many and many a time.
Both of us born in Changgan, you and I!
Why haven't we always known each other?"
255
Folk-song-styled-verse
Li Bai
A SIGH FROM A STAIRCASE OF JADE
Her jade-white staircase is cold with dew;
Her silk soles are wet, she lingered there so long....
Behind her closed casement, why is she still waiting,
Watching through its crystal pane the glow of the autumn moon?
256
Folk-song-styled-verse
Lu Lun
BORDER-SONGS I
His golden arrow is tipped with hawk's feathers,
His embroidered silk flag has a tail like a swallow.
One man, arising, gives a new order
To the answering shout of a thousand tents.
257
Folk-song-styled-verse
Lu Lun
BORDER-SONGS II
The woods are black and a wind assails the grasses,
Yet the general tries night archery --
And next morning he finds his white-plumed arrow
Pointed deep in the hard rock.
258
Folk-song-styled-verse
Lu Lun
BORDER-SONGS III
High in the faint moonlight, wildgeese are soaring.
Tartar chieftains are fleeing through the dark --
And we chase them, with horses lightly burdened
And a burden of snow on our bows and our swords.
259
Folk-song-styled-verse
Lu Lun
BORDER-SONGS IV
Let feasting begin in the wild camp!
Let bugles cry our victory!
Let us drink, let us dance in our golden armour!
Let us thunder on rivers and hills with our drums!
260
Folk-song-styled-verse
Li Yi
A SONG OF THE SOUTHERN RIVER
Since I married the merchant of Qutang
He has failed each day to keep his word....
Had I thought how regular the tide is,
I might rather have chosen a river-boy.
261
Seven-character-quatrain
He Zhizhang
COMING HOME
I left home young. I return old;
Speaking as then, but with hair grown thin;
And my children, meeting me, do not know me.
They smile and say: "Stranger, where do you come from?"
262
Seven-character-quatrain
Zhang Xu
PEACH-BLOSSOM RIVER
A bridge flies away through a wild mist,
Yet here are the rocks and the fisherman's boat.
Oh, if only this river of floating peach-petals
Might lead me at last to the mythical cave!
263
Seven-character-quatrain
Wang Wei
ON THE MOUNTAIN HOLIDAY
THINKING OF MY BROTHERS IN SHANDONG
All alone in a foreign land,
I am twice as homesick on this day
When brothers carry dogwood up the mountain,
Each of them a branch-and my branch missing.
264
Seven-character-quatrain
Wang Changling
AT HIBISCUS INN
PARTING WITH XIN JIAN
With this cold night-rain hiding the river, you have come into Wu.
In the level dawn, all alone, you will be starting for the mountains of
Chu.
Answer, if they ask of me at Loyang:
"One-hearted as ice in a crystal vase."
265
Seven-character-quatrain
Wang Changling
IN HER QUIET WINDOW
Too young to have learned what sorrow means,
Attired for spring, she climbs to her high chamber....
The new green of the street-willows is wounding her heart --
Just for a title she sent him to war.
266
Seven-character-quatrain
Wang Changling
A SONG OF THE SPRING PALACE
Last night, while a gust blew peach-petals open
And the moon shone high on the Palace Beyond Time,
The Emperor gave Pingyang, for her dancing,
Brocades against the cold spring-wind.
267
Seven-character-quatrain
Wang Han
A SONG OF LIANGZHOU
They sing, they drain their cups of jade,
They strum on horseback their guitars.
...Why laugh when they fall asleep drunk on the sand ? --
How many soldiers ever come home?
268
Seven-character-quatrain
Li Bai
A FAREWELL TO MENG HAORAN
ON HIS WAY TO YANGZHOU
You have left me behind, old friend, at the Yellow Crane Terrace,
On your way to visit Yangzhou in the misty month of flowers;
Your sail, a single shadow, becomes one with the blue sky,
Till now I see only the river, on its way to heaven.
269
Seven-character-quatrain
Li Bai
THROUGH THE YANGZI GORGES
From the walls of Baidi high in the coloured dawn
To Jiangling by night-fall is three hundred miles,
Yet monkeys are still calling on both banks behind me
To my boat these ten thousand mountains away.
270
Seven-character-quatrain
Cen Can
ON MEETING A MESSENGER TO THE CAPITAL
It's a long way home, a long way east.
I am old and my sleeve is wet with tears.
We meet on horseback. I have no means of writing.
Tell them three words: "He is safe."
271
Seven-character-quatrain
Du Fu
ON MEETING LI GUINIAN DOWN THE RIVER
I met you often when you were visiting princes
And when you were playing in noblemen's halls.
...Spring passes.... Far down the river now,
I find you alone under falling petals.
272
Seven-character-quatrain
Wei Yingwu
AT CHUZHOU ON THE WESTERN STREAM
Where tender grasses rim the stream
And deep boughs trill with mango-birds,
On the spring flood of last night's rain
The ferry-boat moves as though someone were poling.
273
Seven-character-quatrain
Zhang Ji
A NIGHT-MOORING NEAR MAPLE BRIDGE
While I watch the moon go down, a crow caws through the frost;
Under the shadows of maple-trees a fisherman moves with his torch;
And I hear, from beyond Suzhou, from the temple on Cold Mountain,
Ringing for me, here in my boat, the midnight bell.
274
Seven-character-quatrain
Han Hong
AFTER THE DAY OF NO FIRE
Petals of spring fly all through the city
From the wind in the willows of the Imperial River.
And at dusk, from the palace, candles are given out
To light first the mansions of the Five Great Lords.
275
Seven-character-quatrain
Liu Fangping
A MOONLIGHT NIGHT
When the moon has coloured half the house,
With the North Star at its height and the South Star setting,
I can fed the first motions of the warm air of spring
In the singing of an insect at my green-silk window.
276
Seven-character-quatrain
Liu Fangping
SPRING HEART-BREAK
With twilight passing her silken window,
She weeps alone in her chamber of gold
For spring is departing from a desolate garden,
And a drift of pear-petals is closing a door.
277
Seven-character-quatrain
Liu Zhongyong
A TROOPER'S BURDEN
For years, to guard the Jade Pass and the River of Gold,
With our hands on our horse-whips and our swordhilts,
We have watched the green graves change to snow
And the Yellow Stream ring the Black Mountain forever.
278
Seven-character-quatrain
Gu Kuang
A PALACE POEM
High above, from a jade chamber, songs float half-way to heaven,
The palace-girls' gay voices are mingled with the wind --
But now they are still, and you hear a water-clock drip in the Court of
the Moon....
They have opened the curtain wide, they are facing the River of Stars.
279
Seven-character-quatrain
Li Yi
ON HEARING A FLUTE AT NIGHT
FROM THE WALL OF SHOUXIANG
The sand below the border-mountain lies like snow,
And the moon like frost beyond the city-wall,
And someone somewhere, playing a flute,
Has made the soldiers homesick all night long.
280
Seven-character-quatrain
Liu Yuxi
BLACKTAIL ROW
Grass has run wild now by the Bridge of Red-Birds;
And swallows' wings, at sunset, in Blacktail Row
Where once they visited great homes,
Dip among doorways of the poor.
281
Seven-character-quatrain
Liu Yuxi
A SPRING SONG
In gala robes she comes down from her chamber
Into her courtyard, enclosure of spring....
When she tries from the centre to count the flowers,
On her hairpin of jade a dragon-fly poises.
282
Seven-character-quatrain
Bai Juyi
A SONG OF THE PALACE
Her tears are spent, but no dreams come.
She can hear the others singing through the night.
She has lost his love. Alone with her beauty,
She leans till dawn on her incense-pillow.
283
Seven-character-quatrain
Zhang Hu
OF ONE IN THE FORBIDDEN CITY
When the moonlight, reaching a tree by the gate,
Shows her a quiet bird on its nest,
She removes her jade hairpins and sits in the shadow
And puts out a flame where a moth was flying.
284
Seven-character-quatrain
Zhang Hu
ON THE TERRACE OF ASSEMBLED ANGELS I
The sun has gone slanting over a lordly roof
And red-blossoming branches have leaned toward the dew
Since the Emperor last night summoned a new favourite
And Lady Yang's bright smile came through the curtains.
285
Seven-character-quatrain
Zhang Hu
ON THE TERRACE OF ASSEMBLED ANGELS II
The Emperor has sent for Lady Guoguo.
In the morning, riding toward the palace-gate,
Disdainful of the paint that might have marred her beauty,
To meet him she smooths her two moth-tiny eyebrows.
286
Seven-character-quatrain
Zhang Hu
AT NANJING FERRY
This one-story inn at Nanjing ferry
Is a miserable lodging-place for the night --
But across the dead moon's ebbing tide,
Lights from Guazhou beckon on the river.
287
Seven-character-quatrain
Zhu Qingyu
A SONG OF THE PALACE
Now that the palace-gate has softly closed on its flowers,
Ladies file out to their pavilion of jade,
Abrim to the lips with imperial gossip
But not daring to breathe it with a parrot among them.
288
Seven-character-quatrain
Zhu Qingyu
ON THE EVE OF GOVERNMENT EXAMINATIONS
TO SECRETARY ZHANG
Out go the great red wedding-chamber candles.
Tomorrow in state the bride faces your parents.
She has finished preparing; she asks of you meekly
Whether her eyebrows are painted in fashion.
289
Seven-character-quatrain
Du Mu
I CLIMB TO THE LEYOU TOMBS
BEFORE LEAVING FOR WUXING
Even in this good reign, how can I serve?
The lone cloud rather, the Buddhist peace....
Once more, before crossing river and sea,
I face the great Emperor's mountain-tomb.
290
Seven-character-quatrain
Du Mu
BY THE PURPLE CLIFF
On a part of a spear still unrusted in the sand
I have burnished the symbol of an ancient kingdom....
Except for a wind aiding General Zhou Yu,
Spring would have sealed both Qiao girls in CopperBird Palace.
291
Seven-character-quatrain
Du Mu
A MOORING ON THE QIN HUAI RIVER
Mist veils the cold stream, and moonlight the sand,
As I moor in the shadow of a river-tavern,
Where girls, with no thought of a perished kingdom,
Gaily echo A Song of Courtyard Flowers.
292
Seven-character-quatrain
Du Mu
A MESSAGE TO HAN CHO THE YANGZHOU MAGISTRATE
There are faint green mountains and far green waters,
And grasses in this river region not yet faded by autumn;
And clear in the moon on the Twenty-Four Bridges,
Girls white as jade are teaching flute-music.
293
Seven-character-quatrain
Du Mu
A CONFESSION
With my wine-bottle, watching by river and lake
For a lady so tiny as to dance on my palm,
I awake, after dreaming ten years in Yangzhou,
Known as fickle, even in the Street of Blue Houses.
294
Seven-character-quatrain
Du Mu
IN THE AUTUMN NIGHT
Her candle-light is silvery on her chill bright screen.
Her little silk fan is for fireflies....
She lies watching her staircase cold in the moon,
And two stars parted by the River of Heaven.
295
Seven-character-quatrain
Du Mu
PARTING I
She is slim and supple and not yet fourteen,
The young spring-tip of a cardamon-spray.
On the Yangzhou Road for three miles in the breeze
Every pearl-screen is open. But there's no one like her.
296
Seven-character-quatrain
Du Mu
Parting II
How can a deep love seem deep love,
How can it smile, at a farewell feast?
Even the candle, feeling our sadness,
Weeps, as we do, all night long.
297
Seven-character-quatrain
Du Mu
THE GARDEN OF THE GOLDEN VALLEY
Stories of passion make sweet dust,
Calm water, grasses unconcerned.
At sunset, when birds cry in the wind,
Petals are falling like a girl s robe long ago.
298
Seven-character-quatrain
Li Shangyin
NOTE ON A RAINY NIGHT TO A FRIEND IN THE NORTH
You ask me when I am coming. I do not know.
I dream of your mountains and autumn pools brimming all night with the
rain.
Oh, when shall we be trimming wicks again, together in your western
window?
When shall I be hearing your voice again, all night in the rain?
299
Seven-character-quatrain
Li Shangyin
A MESSAGE TO SECRETARY LINGHU
I am far from the clouds of Sung Mountain, a long way from trees in Qin;
And I send to you a message carried by two carp:
-- Absent this autumn from the Prince's garden,
There's a poet at Maoling sick in the rain.
300
Seven-character-quatrain
Li Shangyin
THERE IS ONLY ONE
There is only one Carved-Cloud, exquisite alwaysYet she dreads the spring, blowing cold in the palace,
When her husband, a Knight of the Golden Tortoise,
Will leave her sweet bed, to be early at court.
301
Seven-character-quatrain
Li Shangyin
THE SUI PALACE
When gaily the Emperor toured the south
Contrary to every warning,
His whole empire cut brocades,
Half for wheel-guards, half for sails.
302
Seven-character-quatrain
LI SHANGYIN
THE JADE POOL
The Mother of Heaven, in her window by the Jade Pool,
Hears The Yellow Bamboo Song shaking the whole earth.
Where is Emperor Mu, with his eight horses running
Ten thousand miles a day? Why has he never come back?
303
Seven-character-quatrain
Li Shangyin
TO THE MOON GODDESS
Now that a candle-shadow stands on the screen of carven marble
And the River of Heaven slants and the morning stars are low,
Are you sorry for having stolen the potion that has set you
Over purple seas and blue skies, to brood through the long nights?
304
Seven-character-quatrain
Li Shangyin
JIASHENG
When the Emperor sought guidance from wise men, from exiles,
He found no calmer wisdom than that of young Jia
And assigned him the foremost council-seat at midnight,
Yet asked him about gods, instead of about people.
305
Seven-character-quatrain
Wen Tingyun
SHE SIGHS ON HER JADE LUTE
A cool-matted silvery bed; but no dreams....
An evening sky as green as water, shadowed with tender clouds;
But far off over the southern rivers the calling of a wildgoose,
And here a twelve-story building, lonely under the moon.
306
Seven-character-quatrain
Zheng Tian
ON MAWEI SLOPE
When the Emperor came back from his ride they had murdered Lady Yang --
That passion unforgettable through all the suns and moons
They had led him to forsake her by reminding him
Of an emperor slain with his lady once, in a well at Jingyang Palace.
307
Seven-character-quatrain
Han Wu
COOLER WEATHER
Her jade-green alcove curtained thick with silk,
Her vermilion screen with its pattern of flowers,
Her eight- foot dragon-beard mat and her quilt brocaded in squares
Are ready now for nights that are neither warm nor cold.
308
Seven-character-quatrain
Wei Zhuang
A NANJING LANDSCAPE
Though a shower bends the river-grass, a bird is singing,
While ghosts of the Six Dynasties pass like a dream
Around the Forbidden City, under weeping willows
Which loom still for three miles along the misty moat.
309
Seven-character-quatrain
Chen Tao
TURKESTAN
Thinking only of their vow that they would crush the Tartars- -
On the desert, clad in sable and silk, five thousand of them fell....
But arisen from their crumbling bones on the banks of the river at the
border,
Dreams of them enter, like men alive, into rooms where their loves lie
sleeping.
310
Seven-character-quatrain
Zhang Bi
A MESSAGE
I go in a dream to the house of Xie
Through a zigzag porch with arching rails
To a court where the spring moon lights for ever
Phantom flowers and a single figure.
311
Seven-character-quatrain
Wumingshi
THE DAY OF NO FIRE
As the holiday approaches, and grasses are bright after rain,
And the causeway gleams with willows, and wheatfields wave in the wind,
We are thinking of our kinsfolk, far away from us.
O cuckoo, why do you follow us, why do you call us home?
312
Folk-song-styled-verse
Wang Wei
A SONG AT WEICHENG
A morning-rain has settled the dust in Weicheng;
Willows are green again in the tavern dooryard....
Wait till we empty one more cup --
West of Yang Gate there'll be no old friends.
313
Folk-song-styled-verse
Wang Wei
A SONG OF AN AUTUMN NIGHT
Under the crescent moon a light autumn dew
Has chilled the robe she will not change --
And she touches a silver lute all night,
Afraid to go back to her empty room.
314
Folk-song-styled-verse
Wang Changling
A SIGH IN THE COURT OF PERPETUAL FAITH
She brings a broom at dawn to the Golden Palace doorway
And dusts the hall from end to end with her round fan,
And, for all her jade-whiteness, she envies a crow
Whose cold wings are kindled in the Court of the Bright Sun.
315
Folk-song-styled-verse
Wang Changling
OVER THE BORDER
The moon goes back to the time of Qin, the wall to the time of Han,
And the road our troops are travelling goes back three hundred miles....
Oh, for the Winged General at the Dragon City --
That never a Tartar horseman might cross the Yin Mountains!
316
Folk-song-styled-verse
Wang Zhihuan
BEYOND THE BORDER
Where a yellow river climbs to the white clouds,
Near the one city-wall among ten-thousand-foot mountains,
A Tartar under the willows is lamenting on his flute
That spring never blows to him through the Jade Pass
317
Folk-song-styled-verse
Li Bai
A SONG OF PURE HAPPINESS I
Her robe is a cloud, her face a flower;
Her balcony, glimmering with the bright spring dew,
Is either the tip of earth's Jade Mountain
Or a moon- edged roof of paradise.
318
Folk-song-styled-verse
Li Bai
A SONG OF PURE HAPPINESS II
There's a perfume stealing moist from a shaft of red blossom,
And a mist, through the heart, from the magical Hill of Wu- -
The palaces of China have never known such beautyNot even Flying Swallow with all her glittering garments.
319
Folk-song-styled-verse
Li Bai
A SONG OF PURE HAPPINESS III
Lovely now together, his lady and his flowers
Lighten for ever the Emperor's eye,
As he listens to the sighing of the far spring wind
Where she leans on a railing in the Aloe Pavilion.
320
Folk-song-styled-verse
Du Qiuniang
THE GOLD-THREADED ROBE
Covet not a gold-threaded robe,
Cherish only your young days!
If a bud open, gather it --
Lest you but wait for an empty bough.
"""

inv_raw = inv_raw.split("\n")

poem_json = dict()
count, key_val = 0, 0

parsed_pdf_content = inv_raw[1:-1]
print(parsed_pdf_content)

for line in parsed_pdf_content:

    if (line.isdigit()):

        key_val = int(line)

        count = 0
        poem_json[int(line)] = dict()

    else:
        if count == 1:
            poem_json[key_val]["style"] = line
        elif count == 2:
            poem_json[key_val]["author"] = line
        elif count == 3:
            poem_json[key_val]["title"] = line
        else:

            if "content" not in poem_json[key_val]:

                poem_json[key_val]["content"] = line
            else:
                poem_json[key_val]["content"] += line
    count += 1


