#python -m streamlit run app.py

import streamlit as st  

st.sidebar.write('PLAYLIST')
generos = {
    'rock' : {
        'Queen': 'https://youtu.be/fJ9rUzIMcZQ?si=cHm3ibLePVnl5Z0y',
        'Nirvana': 'https://youtu.be/hTWKbfoikeg?si=Ghrx7sTYNsgmpYuJ',
        'Guns N Roses': 'https://youtu.be/dpmAY059TTY?si=rx341_30-cnExvD-',
        'Maneskin': 'https://youtu.be/odWKEfp2QMY?si=St6z7vWnCu0ZJtN6'
        
    },
    'hip-hop': {
        'eminen': 'https://youtu.be/YVkUvmDQ3HY?si=nfOjR9nyJXvCtPya',
        'sabotage': 'https://youtu.be/GA7LcSX8tYE?si=rZ6w1cJ1k7KQ3our',
        'keyne west': 'https://youtu.be/MKM90u7pf3U?si=k7XW_epwR2kH4fBC',
        'racionais mcs': 'https://youtu.be/ryP3ZvRPJhY?si=bH6z3_IVBE5A1d22'
    
    },
    'pop': {
        'michael jackson': 'https://youtu.be/Zi_XLOBDo_Y?si=rv3S5-uEl01vO0eY',
        'justin timberlake': 'https://youtu.be/uuZE_IRwLNI?si=fufLHyXdvosTPgFx',
        'Damiano david': 'https://youtu.be/Z4-g8UXa944?si=KRplA5lc2MK3K6PT',
        'Bruno mars ': 'https://youtu.be/fLexgOxsZu0?si=hLlnna37cg6lbThu'

    },
    'classicas': {
        'beethoven': 'https://youtu.be/4Tr0otuiQuU?si=R476w2LY5AOMwUo6',
        'Emilo piano': 'https://youtu.be/dyQWKEjjDMM?si=dnAlq-lfq3e3x438',
        'Frédéric Chopin ': 'https://youtu.be/hZY5DBmgC_A?si=Y0BMGGFxcYa5J_nk',
        'Andrea Bocelli': 'https://youtu.be/TdWEhMOrRpQ?si=Rt3acBGCVw51dsNA'

}
}
#-------------------------------------------sidebar
st.sidebar.title('PLAYLIST MISTÃO ')
st.sidebar.image('playlist.png')


genero = st.sidebar.selectbox('escolha um genero musical', generos.keys() )
artista = st.sidebar.selectbox('escolha um artista', generos[genero])

#----------------------------------------------bory
st.title(artista)
st.markdown('---')

video,sobre = st.tabs(['videos', 'sobre o artista'])

with video: 
    st.video(generos[genero][artista])
with sobre: 
    if artista == 'Queen': 
        st.markdown('''
Queen foi uma banda britânica de rock, fundada em 1970 e ativa, sob sua formação clássica, até 1991. O grupo, formado por Brian May (guitarra e vocais), Freddie Mercury (vocais e piano), John Deacon (baixo) e Roger Taylor (bateria e vocais), é frequentemente citado como um dos expoentes do seu estilo, também sendo um dos recordistas de vendas de discos a nível mundial. A música da banda também é conhecida por ser altamente eclética, variando entre várias vertentes do rock.

Originalmente, a banda surgiu a partir do trio Smile, formado por Brian May, Roger Taylor e o baixista Tim Staffell. Com o fim do conjunto, Freddie Mercury e John Deacon, juntamente com May e Roger, estabeleceram a formação de um novo grupo em meados de 1970. Os seus dois primeiros álbuns alcançaram pouco sucesso, até que ganhou popularidade internacional por meio de Sheer Heart Attack (1974) e, principalmente, por A Night at the Opera (1975), cujos singles "Bohemian Rhapsody" e "You're My Best Friend" alcançaram bons desempenhos. Mais tarde, a popularidade do quarteto estendeu-se com News of the World, em 1977, devido aos hits "We Will Rock You" e "We Are the Champions", bem como com "Crazy Little Thing Called Love" e "Another One Bites the Dust", de The Game, lançado em 1980.

Durante a década de 1980, o Queen passou a adotar sintetizadores nas suas músicas, e apesar de alguns sucessos como "Under Pressure", a banda recebeu fortes críticas da mídia especializada, perdeu grande parte de sua popularidade em território norte-americano, e passou por crises internas. Em meio às críticas, a banda ainda lançou sucessos: O álbum The Works (1984) conteve os singles "Radio Ga Ga" e "I Want to Break Free", que alcançaram notoriedade no Reino Unido e em países da América do Sul, como o Brasil e Argentina. Em 1985, o conjunto realizou uma das suas performances mais memoráveis no evento Live Aid, e em 1986 a última turnê. Em 1987, o vocalista Freddie Mercury contraiu o vírus do HIV. Com isso, a banda continuou produzindo trabalhos que se tornaram os últimos registros em vida de seu cantor. The Miracle (1989) e Innuendo (1991) foram melhor recebidos que os anteriores, e também ganharam avaliações mais positivas após a morte de Freddie. Brian, Roger e John trabalharam em algumas faixas arquivadas durante dois anos e, com isso, foi lançado o último trabalho inédito do quarteto, Made in Heaven (1995). Em 1997, o baixista John Deacon aposentou-se do mundo musical.

Nos anos seguintes, Brian May e Roger Taylor seguiram carreiras a solo, tocaram com vários músicos convidados e, com o repertório do Queen, chegaram a se apresentar com artistas como Elton John. Como shows com o nome da banda, destacam-se as parcerias feitas com Paul Rodgers e Adam Lambert, com quem formaram, respectivamente, os supergrupos Queen + Paul Rodgers (entre 2004 a 2009) e Queen + Adam Lambert (de 2011 aos dias atuais). A banda já vendeu mais de trezentos milhões de discos ao redor do mundo, tendo lançado quinze álbuns inéditos, várias coletâneas e trabalhos em vídeo. O grupo foi incluído no Rock and Roll Hall of Fame em 2001 e todos os seus integrantes foram introduzidos ao Songwriters Hall of Fame em 2003. Além disso, ganhou uma estrela no Passeio da Fama em Hollywood em 2005 e é apontado como influência para vários artistas do cenário rock e pop, bem como foi tema do musical We Will Rock You e do filme Bohemian Rhapsody, de 2018.
''')
    elif artista == 'Guns N Roses':
        st.markdown('''
Guns N' Roses[nota 1] é uma banda americana de hard rock formada em Los Angeles, Califórnia, em 1985, resultado da fusão entre as bandas locais L.A. Guns e Hollywood Rose. A formação original do grupo era composta pelo vocalista Axl Rose, o baixista Ole Beich, o baterista Rob Gardner e os guitarristas Tracii Guns e Izzy Stradlin. Meses depois, após assinarem com a Geffen Records, a formação "clássica" do grupo contava com Rose, Stradlin, o guitarrista Slash, o baixista Duff McKagan e o baterista Steven Adler. A formação atual inclui Rose, Slash, McKagan, o guitarrista Richard Fortus, os tecladistas Dizzy Reed e Melissa Reese e o baterista Isaac Carpenter.

Nos primeiros anos, o hedonismo e a rebeldia da banda levaram a comparações com os primeiros The Rolling Stones e lhes renderam o apelido de "a banda mais perigosa do mundo". A banda percorreu extensivamente o circuito de clubes da Costa Oeste dos Estados Unidos durante os seus primórdios. Controvérsias significativas seguiram a banda devido a atrasos em apresentações ao vivo e tumultos, letras consideradas problemáticas, a personalidade franca de Rose, problemas com drogas e com álcool de vários outros membros, processos judiciais e disputas públicas com outros artistas. O seu álbum de estreia, Appetite for Destruction, de 1987, lançado junto à turnê homônima, inicialmente teve um desempenho modesto, estreando na posição 182 da Billboard 200. No entanto, um ano após o lançamento, uma campanha espontânea impulsionada pelo videoclipe de "Welcome to the Jungle" trouxe à banda grande popularidade. "Welcome to the Jungle" e "Paradise City" tornaram-se sucessos no top 10, enquanto "Sweet Child o' Mine" foi o único single da banda a alcançar o primeiro lugar na Billboard Hot 100. O álbum vendeu aproximadamente 30 milhões de cópias em todo o mundo, incluindo 18 milhões apenas nos Estados Unidos, tornando-se o álbum de estreia mais vendido do país e o 11.º mais vendido da história. Com sua fusão de punk rock, blues rock e heavy metal, o grupo ajudou a afastar o rock mainstream da era do glam metal dos anos 1980. Além disso, são creditados por revitalizar as power ballads no rock. O segundo álbum de estúdio, G N' R Lies, de 1988, combinou o EP inicial Live ?!@ Like a Suicide, de 1986, com novas faixas acústicas. O disco atingiu a segunda posição na Billboard 200, vendeu 10 milhões de cópias mundialmente (incluindo cinco milhões nos Estados Unidos) e trouxe o sucesso top 5 "Patience" e "One in a Million". Em 1989, Rose convidou Reed para se juntar à banda como tecladista, entrando oficialmente em 1990, durante as gravações dos álbuns Use Your Illusion I e Use Your Illusion II. No mesmo ano, o baterista Steven Adler foi demitido devido ao seu vício em drogas e substituído por Matt Sorum, que ficou até 1997.

Os terceiro e quarto álbuns da banda, Use Your Illusion I e Use Your Illusion II, foram gravados e lançados simultaneamente em 1991. Eles estrearam, respectivamente, nas posições dois e um da Billboard 200 e acumularam vendas combinadas de 35 milhões de cópias no mundo todo (incluindo 14 milhões nos Estados Unidos). Os discos trouxeram sucessos como "You Could Be Mine", versões cover de "Live and Let Die" e "Knockin' on Heaven's Door", além de uma trilogia de ballads "Don't Cry", "November Rain" e "Estranged", acompanhadas por videoclipes de alto orçamento. Os álbuns foram promovidos pela turnê mundial Use Your Illusion Tour, que durou de 1991 a 1993 e se tornou uma das turnês mais assistidas da história. Durante o início da turnê, Stradlin deixou abruptamente a banda em 1991 e foi substituído por Gilby Clarke. Em 1993, o grupo lançou The Spaghetti Incident?, um álbum de covers de punk rock e hard rock. Apesar da recepção relativamente positiva, foi o álbum de estúdio com menor desempenho comercial da banda até então e não contou com uma turnê de divulgação. Esse foi o último álbum de estúdio a contar com Stradlin e Matt Sorum, o único com a participação de Clarke e o último a incluir Slash e McKagan.
''')
    elif artista == 'Maneskin': 
        st.markdown('''
Måneskin é uma banda de hard rock[1] italiana formada em Roma no ano de 2016. Ganharam fama na Itália após a participação na 11ª edição do Factor X. Mesmo tendo ficado em 2º lugar, conseguiram assinar um contrato com a Sony Music. Chosen (EP) foi o 1º álbum da banda, lançado em 2017.[2] Com a canção "Zitti e Buoni" sagraram-se vencedores do Festival Eurovisão da Canção 2021.[3]

História
Início
A banda foi formada em 2016 por Victoria De Angelis e Thomas Raggi, ambos estudavam na "Scuola Media Gianicolo", no bairro romano de Monteverde, tempo depois juntaram-se Damiano David e Ethan Torchio. O nome da banda "Måneskin" significa "clarão da lua" ou "luar" em dinamarquês, e surgiu de um brainstorming onde Victoria, que é filha de mãe dinamarquesa e pai italiano, teve de dizer palavras ao calhas naquela língua. Embora aquela palavra tenha sido a escolhida como nome, não tem muita relação com o tipo de música que fazem.[4]

The X-Factor
No ano de 2017, a banda participou da 11.ª edição da versão italiana do Factor X, e ficaram em 2.º lugar. No decorrer do concurso, a banda lançou o seu primeiro EP chamado "Chosen"[5] o qual acabaria por receber dois discos de platina por parte da Federazione Industria Musicale Italiana.[6]

A 7 de janeiro de 2018, a banda foi convidada ao programa Che tempo che fa, da Rai 1, sendo esta a primeira aparição na televisão pública de Itália.[7] A 23 de março de 2018, a banda lançou o seu segundo single, chamado "Morirò da re" que recebeu três discos de platina.[3][6]

Em junho de 2018, a banda recebeu um disco de platina pelo álbum Chosen no Wind Music Awards, em Verona.[8] Em 6 de setembro, abriam o concerto dos Imagine Dragons em Milão.[9]
''')
    elif artista == 'Nirvana': 
        st.markdown('''
Nirvana foi uma banda estadunidense de rock formada pelo vocalista e guitarrista Kurt Cobain e pelo baixista Krist Novoselic em Aberdeen no ano de 1987,[1] que obteve grande sucesso no movimento grunge de Seattle no início dos anos 1990. Vários bateristas passaram pelo Nirvana, sendo o que ficou mais tempo na banda foi Dave Grohl, que entrou em 1990.

No final da década de 1980 o Nirvana se estabeleceu como parte da cena grunge de Seattle, lançando o seu primeiro álbum, Bleach, pela gravadora independente Sub Pop em 1989. A banda desenvolveu um som que se baseava em contrastes dinâmicos, muitas vezes entre versos calmos e barulhentos, e refrões pesados. Depois de assinar com a gravadora DGC Records, o grupo encontrou o sucesso inesperado com "Smells Like Teen Spirit", o primeiro single do segundo álbum da banda, Nevermind (1991). O sucesso repentino da banda amplamente popularizou o rock alternativo como um todo, e como o vocalista da banda, Cobain se encontrou referido na mídia como o "porta-voz de uma geração", com o Nirvana sendo considerado a "principal banda" da Geração X.[2] Nevermind é citado como um dos melhores álbuns de todos os tempos, e contém três singles na lista de "500 Maiores Canções de Todos os Tempos", da revista Rolling Stone. O terceiro álbum de estúdio do Nirvana, In Utero (1993), desafiou a audiência do grupo, apresentando um som abrasivo, natural e cru, menos mainstream. In Utero, apesar de ser um álbum que se volta contra o sistema (fama e mídia), também foi muito bem-sucedido, surpreendendo a crítica, os produtores, e até mesmo a própria gravadora.
''')

    elif artista == 'Damiano david':
        st.markdown('''
Damiano David (Roma, 8 de janeiro de 1999)[1] é um cantor e compositor italiano, mais conhecido por ser o vocalista da banda de rock italiana Måneskin, que venceu a edição de 2021 do Festival de Sanremo e posteriormente o Festival Eurovisão da Canção 2021 (este último enquanto representante italiano) com a canção "Zitti e buoni".[2][3] Ele é conhecido pelo seu "carisma natural dos grandes frontmen",[4] e como um ícone da moda italiana.[5] David estreou sua carreira solo com a faixa "Silverlines". Lançada em 27 de setembro de 2024, a música foi feita em colaboração com o produtor Labrinth (que produz a trilha da série “Euphoria") e demonstra um lado mais emocional e pop do cantor de 25 anos.[6]
''')
    elif artista == 'justin timberlake': 
        st.markdown('''Justin Randall Timberlake (Memphis, 31 de janeiro de 1981) é um cantor, compositor, ator, produtor musical, dançarino, multi-instrumentista e empresário norte-americano.[4]

Ex-integrante da boy band 'N Sync, Timberlake lançou em 2002 seu primeiro álbum em carreira solo, Justified, que vendeu mais de sete milhões de cópias mundialmente.[5] Em seguida lançou singles que marcaram a sua carreira, como "Cry Me a River" e "Rock Your Body", que o fizeram ganhar seus dois primeiros Grammys e seus três primeiros VMAs. Seu segundo álbum de estúdio, FutureSex/LoveSounds, foi lançado em setembro de 2006 e vendeu mais de 14 milhões de cópias no mundo,[5] além de ter garantido a 1ª posição em muitos países, colocando três singles em primeiro lugar na lista do mais populares dos Estados Unidos: "SexyBack", "My Love" e "What Goes Around... Comes Around", e ter rendido a Justin mais quatro Grammys e quatro VMAs.

Sete anos depois, lançou seu terceiro álbum de estúdio, The 20/20 Experience, que debutou em primeiro lugar nos Estados Unidos e Reino Unido,[6][7] e lançou singles como "Suit & Tie" e "Mirrors" que alcançaram o top 3 da Billboard Hot 100, além de ter sido o álbum mais vendido dos Estados Unidos, no ano de 2013.[8] No mesmo ano, lançou seu quarto álbum de estúdio, The 20/20 Experience 2 of 2, que também ficou em primeiro lugar em vários países, e lançou singles como "Not a Bad Thing", que também teve bom desempenho nas tabelas musicais, alcançando a 8ª posição no Hot 100. Os dois álbuns renderam a Justin mais três Grammys, e mais quatro VMAs. Em 2016, Justin participou da trilha sonora do filme Trolls, filme na qual ele dublou um personagem e lançou um single, Can't Stop the Feeling!. A música fez bastante sucesso, estreando já na primeira colocação da Billboard Hot 100. Além disso, a música ganhou um Grammy e foi indicada para o Óscar e para o Globo de Ouro.''')
    elif artista == 'michael jackson':
        st.markdown('''
Michael Joseph Jackson (Gary, 29 de agosto de 1958 – Los Angeles, 25 de junho de 2009) foi um cantor, compositor, dançarino e filantropo estadunidense. Apelidado de "Rei do Pop", ele é considerado uma das figuras culturais mais significantes do século XX e um dos maiores artistas da história da música. Ao longo de uma carreira de quatro décadas, suas conquistas musicais ao redor do mundo e sua vida pessoal publicizada fizeram dele uma figura global na cultura popular. Por meio da música, dança e moda, ele proliferou a performance visual para cantores de música pop, e popularizou movimentos da dança de rua, incluindo o moonwalk (que ele nomeou), o robô e a inclinada anti-gravidade. Jackson possui uma extensa legião de fãs, que inclui imitadores de todo o mundo.

O oitavo filho da família Jackson, Michael fez sua estreia profissional aos seis anos de idade em 1964, com seus irmãos mais velhos, Jackie, Tito, Jermaine e Marlon, como membro do grupo musical The Jackson 5. O grupo assinou com a Motown em 1968 e conquistou sucesso mundial com Michael como vocalista principal. Jackson alcançou o estrelato como solista com o lançamento de seu quinto álbum de estúdio, Off the Wall (1979). No início dos anos 1980, Michael se tornou uma figura dominante na música popular com o lançamento de Thriller (1982), o álbum mais vendido de todos os tempos. Os videoclipes inovadores de sua faixa-título, juntamente com "Beat It" e "Billie Jean", são creditados por quebrar barreiras raciais e transformar o meio em uma forma de arte e ferramenta promocional, bem como contribuíram para a popularização da MTV. Jackson solidificou sua posição como uma superestrela global com Bad (1987), o primeiro álbum a produzir cinco singles que alcançaram a primeira posição da Billboard Hot 100: "I Just Can't Stop Loving You", "Bad", "The Way You Make Me Feel", "Man in the Mirror" e "Dirty Diana". Dangerous (1991) o viu se aventurar em uma variedade de sons artísticos e se tornou um dos álbuns de maior sucesso da década de 1990. HIStory: Past, Present and Future, Book I (1995) produziu "You Are Not Alone", a primeira canção a estrear no topo da Billboard Hot 100.

No final dos anos 1980, Jackson se tornou uma figura de controversa por sua radical mudança de aparência, relacionamentos, comportamento e estilo de vida. Em 1993, ele foi acusado de abusar sexualmente do filho de um amigo da família. Em 2005, ele foi julgado e absolvido de outras acusações de abuso sexual infantil e várias outras acusações. Em 2009, enquanto se preparava para a turnê This Is It, Jackson morreu de overdose de sedativos administrados por seu médico pessoal Conrad Murray, que foi condenado em 2011 por homicídio culposo. A morte de Jackson desencadeou reações em todo o mundo, criando picos sem precedentes de tráfego na Internet e um aumento nas vendas de sua música. Estima-se que seu funeral público, realizado no Staples Center, em Los Angeles, tenha sido visto por mais de 2.5 bilhões de pessoas.

Jackson é um dos artistas musicais mais vendidos de todos os tempos, com vendas estimadas em mais de 500 milhões de discos em todo o mundo. Ele venceu múltiplos prêmios, tornando-o um dos artistas mais premiados da música popular. Suas conquistas incluem 39 recordes no Guinness World Records (incluindo o de Artista Mais Bem Sucedido de Todos os Tempos), 15 Grammy Awards (incluindo os prêmios Legend e Lifetime Achievement), 26 American Music Awards (incluindo os prêmios de Artista do Século e Artista da Década de 1980) e seis Brit Awards. Ele também recebeu três honras presidenciais, incluindo Artista da Década, e o prêmio Bambi de Artista Pop do Milênio. Ele teve 13 canções número um da Billboard Hot 100 e foi o primeiro artista a ter uma canção no top dez da tabela em cinco décadas diferentes. As induções de Jackson incluem o Rock and Roll Hall of Fame (duas vezes), o National Rhythm & Blues Hall of Fame, o Vocal Group Hall of Fame, o Songwriters Hall of Fame e o Dance Hall of Fame (tornando-o o único artista a ser induzido). Em 2016, o patrimônio de Jackson era de 825 milhões de dólares, o valor anual mais alto de uma celebridade já registrada pela Forbes.[1]
''')
    elif artista == 'Bruno mars ': 
        st.markdown('''
Peter Gene Hernandez (Honolulu, 8 de outubro de 1985),[1] mais conhecido pelo nome artístico Bruno Mars,[2] é um cantor, compositor, músico e dançarino americano. Vindo de uma família com uma grande tradição musical, Mars começou a cantar e a se apresentar como um artista amador durante a infância. Depois de se formar no Ensino Médio, decidiu mudar-se para Los Angeles, na Califórnia, com o objetivo de investir cada vez mais em sua carreira musical. Em Los Angeles, ele formou a equipe de produtores The Smeezingtons, ao lado de Philip Lawrence e Ari Levine, trabalhando para a Motown Records.

Depois do seu término com a gravadora Motown Records (a mesma onde artistas como The Jackson 5 e Michael Jackson iniciaram suas carreiras), Mars assinou com a Atlantic Records em 2009. Durante os primeiros meses como artista da editora, ele coescreveu os arranjos e fez participações em músicas como "Nothin' on You" (2010), do rapper B.o.B, e "Billionaire" (2010), do cantor americano Travie McCoy. Também participou da composição dos êxitos mundiais "Right Round" (2009), do rapper Flo Rida com participação de Kesha, "Wavin' Flag" (2010), do cantor somali K'naan, e "Fuck You!" (2010), de Cee Lo Green. Em Outubro de 2010, lançou o seu álbum de estúdio de estreia, Doo-Wops & Hooligans. O álbum atingiu o seu pico na terceira colocação da tabela musical Billboard 200 nos Estados Unidos da América, e recebeu o certificado de disco de platina pela Recording Industry Association of America (RIAA) após vender mais de um milhão de cópias no país. Seu primeiro single como artista principal, "Just The Way You Are" (2010), ocupou a primeira posição da tabela de "singles" americana "Billboard Hot" 100 por quatro semanas consecutivas."Grenade" (2010), ocupou a mesma posição por oito semanas não consecutivas. O sucesso dos dois singles nos Estados Unidos fazem de Mars um dos seis artistas masculinos na história que alcançaram o topo da Billboard com os dois primeiros singles do mesmo álbum, e o primeiro a fazê-lo em treze anos. Inspirado por lendários artistas como Michael Jackson e Elvis Presley, o intérprete é considerado um dos mais "versáteis e completos artistas de música pop da atualidade", segundo um crítico do prestigiado jornal The New York Times.[3]
''')
    elif artista == 'eminen':
        st.markdown('''
Marshall Bruce Mathers III (St. Joseph, 17 de outubro de 1972) mais conhecido pelo seu nome artístico Eminem, é um rapper, compositor, produtor musical e ator americano.[2] Adquiriu rápida popularidade em 1999 com o lançamento do disco The Slim Shady LP, o qual venceu o Grammy Award de Melhor Álbum de Rap do ano.[3] O seu próximo trabalho, The Marshall Mathers LP, se tornou o álbum solo mais vendido na história dos Estados Unidos.[4] Tal fato o tornou conhecido no mundo inteiro, e ajudou para a divulgação de sua gravadora, a Shady Records, e do seu grupo, o D12.

The Marshall Mathers LP e o seu terceiro disco, The Eminem Show, também conquistaram o Grammy Awards, tornando ele o primeiro artista a conquistar o prêmio de Melhor Álbum de Rap do ano por três vezes consecutivas. Em 2003, venceu o Oscar de melhor canção original com "Lose Yourself", que esteve presente no seu filme semi-biográfico, 8 Mile. "Lose Yourself" iria se tornar o single que por maior tempo ocupou a primeira posição das paradas de hip hop.[5] Em 2004, boatos sobre o fim de sua carreira foram anunciados após o lançamento do álbum Encore, que foram encerrados com o anunciação de Relapse, oficialmente disponibilizado em 15 de maio de 2009. De acordo com a Nielsen SoundScan, Eminem é o artista que mais vendeu na década nos Estados Unidos e atualmente está na 30ª posição de recordistas de vendas de discos da história do país segundo o ranking da RIAA,[6] e no mundo tem cerca de 115 milhões de álbuns vendidos,[7] tornando-o um dos artistas recordistas de vendas de discos.[8][9] Em 2010, lançou Recovery, no qual estava presente o single "Love the Way You Lie", que foi um enorme sucesso comercial. Recovery tornou-se o sexto álbum consecutivo de Eminem a estrear na primeira posição das paradas do Estados Unidos. De início, o álbum ficou por cinco semanas consecutivas no topo, retornando posteriormente para outras duas, e somando sete semanas em primeiro lugar, no total.[10]

Eminem foi escolhido como o 79º na lista dos "100 Melhores Artistas de Todos os Tempos" da VH1.[11] Em uma lista similar, foi ranqueado em 82º pela revista Rolling Stone.[12] Incluindo o trabalho com o D12, Eminem acumula 12 álbuns no topo da Billboard Top 200, sendo 10 solo (9 de estúdio, 1 compilação) e 2 com o D12. Ele tem 13 singles na primeira posição em todo o mundo.[13] Tal sucesso fez Eminem ser reconhecido pela Billboard como o Artista da Década.[14] De acordo com a mesma Billboard, o rapper teve dois dos cinco álbuns mais vendidos entre 2000 e 2007.[14] Eminem também já vendeu mais de 90 milhões de downloads de suas músicas apenas nos Estados Unidos.[15] Em 2010, a MTV classificou Eminem como o sétimo maior ícone da história da música pop.[16] Em 2009, Eminem foi eleito, em votação popular, o melhor rapper de todos os tempos pela revista Vibe, vencendo Tupac na final.[17] As letras das composições de Eminem são violentamente misógenas e homofóbicas e com um vocabulário bastante vulgar e limitado, e por vários críticos considerado discurso de ódio.[18][19][20]
''')
    elif artista == 'keyne west':
        st.markdown('''
John Maynard Keynes (1883-1946) foi um economista inglês, um dos mais importantes economistas da primeira metade do século XX, considerado por muitos o precursor da economia moderna "a macroeconomia".

John Maynard Keynes nasceu em Cambridge, Inglaterra, no dia 5 de junho de 1883. Filho do economista John Neville Keynes foi educado em um colégio em Elton e no King’s College da Universidade de Cambridge. Em 1905 graduou-se em Matemática recebendo orientação do professor e economista Alfred Marshall que o aproximou cada vez mais dos temas ligados à economia.

Em 1906, John Maynard seguiu para a Índia onde trabalhou no serviço administrativo britânico, permanecendo durante dois anos, experiência que resultou na publicação de seu primeiro livro sobre economia “Indian Currency and Finance” (1913). Em 1909 foi nomeado professor de economia no King’s College de Cambridge, onde permaneceu até 1915. Dividia seu tempo como editor do Economic Journal, até 1945.

Após sair de Cambridge, foi designado para trabalhar no Tesouro Britânico, com a missão de preparar a delegação do país que seria enviada para negociar no Tratado de Versalles depois da derrota da Alemanha na Primeira Guerra Mundial (1914-1918). Por não concordar com as duras condições impostas aos vencidos, demitiu-se do cargo e em seguida publicou “As Consequências Econômicas da Paz” (1919), para argumentar que tais condições seriam impossíveis de se cumprir e levaria à ruína econômica da Alemanha, com graves consequências para o resto do mundo. O tempo mostrou que as previsões de Keynes eram acertadas. Ainda sobre o tema escreveu “A Revision of the Treeaty” (1922).

''')
    elif artista == 'racionais mcs':
        st.markdown('''
Racionais MC's é um grupo brasileiro de rap fundado em 1988 na cidade de São Paulo.[2][3] É formado por Pedro Paulo Soares Pereira (Mano Brown), Paulo Eduardo Salvador (Ice Blue), Edivaldo Pereira Alves (Edi Rock) e Kleber Geraldo Lelis Simões (KL Jay).[1][4][5] É o maior grupo de rap do Brasil, e está entre os grupos musicais mais influentes do país e da música brasileira.[6][7][8][9][10] Suas canções demonstram a preocupação em denunciar a destruição da vida de jovens negros e pobres das periferias brasileiras e o resultado do racismo e da violência policial, ao sustentarem a miséria diretamente ligada com a violência e o crime.[11][12][13][14] Temas como a brutalidade da polícia, do crime organizado e do estado, bem como o preconceito, as drogas e a exclusão social são recorrentes nas letras do conjunto.[15][16][17][18] Embora inicialmente conhecido apenas na capital paulista, o grupo conseguiu alcançar sucesso nacional e internacional a partir dos álbuns Raio X Brasil (1993), Sobrevivendo no Inferno (1997)[19][20] e Nada como um Dia após o Outro Dia (2002).[1][21]
''')
    elif artista == 'sabotage':
        st.markdown('''
Mauro Mateus dos Santos (São Paulo, 3 de abril de 1973 – São Paulo, 24 de janeiro de 2003), mais conhecido pelo seu nome artístico Sabotage, foi um rapper, cantor, compositor e ator brasileiro. Mauro, pai de dois filhos, nasceu na Favela do Canão, Zona Sul de São Paulo, onde, depois de ter sido assaltante e gerente de tráfico encontrou a saída no rap, entrando na música e percebendo o seu verdadeiro dom. A origem do apelido Sabotage deu-se por estar sempre conseguindo burlar as leis com tremendo êxito, como entrar em bailes, festas e boates sem permissões, e saindo ileso de inúmeras confusões. Considerado uma lenda na Zona Sul, ele inspirou vários rappers, como Rhossi, Pavilhão 9, além de ter ensinado Paulo Miklos como ser um digno malandro, no filme O Invasor, de Beto Brant, com quem chegou a escrever uma música.[1][2]

No ano 2000, Sabotage lançou seu álbum de estreia, Rap é Compromisso!, e durante sua carreira participou de vários CDs com os grupos RZO, SP Funk, entre outros. Em 2016, treze anos após sua morte, o álbum que leva o mesmo nome do cantor foi lançado no serviço de streaming Spotify. Nele estão diversas canções feitas na semana em que o rapper foi assassinado.[3]

Também, como ator, fez parte de dois filmes, o já citado O Invasor, e o premiado Carandiru, além de ter recebido vários prêmios, como personalidade, revelação e outros no Hútus, o grande festival de premiação de rap no Brasil. Vale ressaltar que Sabotage era o próprio compositor e cantor de suas músicas.[4] Em toda sua carreira, compôs dezenas de trabalhos e alguns deles se tornaram uma espécie de hino para jovens da periferia. Para muitos, Sabotage é uma rica expressão da constante luta que o pobre enfrenta diariamente para viver dignamente e isso fez com que vários outros artistas usassem suas obras como samples, colagens e scratches de seus trabalhos.[5]

Biografia
Vida pessoal e carreira

Graffiti Sabotage em desenho artístico a partir de dezembro de 2013.
Quando era bandido se via naquela música "O Meu Guri", de Chico Buarque e se imaginava cantando. Em 1985, ele escreveu uma música e ensaiou, mas só pra ele mesmo. E usava o solo de uma música do Leo Jaime, pra cantar a sua rima em cima. Ouvia Afrika Bambaataa, Barry White. Dentre todos esses artistas ele se identificou muito com Barry White porque, como ele, Sabotage também perdeu seu irmão para o crime. Desde pequeno tinha mania de andar com uma arma para assaltar pessoas. As pessoas diziam:

“	"Meu, você é louco! Vai puxar uma carroça, pegar um papelão, jornal, levar um dinheiro pra casa."	”
E depois de ter sido reconhecido como rapper, elas se desculpavam: "Meu, eu não devia ter te falado aquilo." Sabotage sempre fez rimas, mas ele nunca se revelava musicalmente a ninguém. Até que em 1988, 1989, começou a se inscrever em concursos de rap. Num deles, no salão Zimbabwe, conheceu Mano Brown e o Ice Blue, ambos do Racionais MC's, que ficaram principalmente impressionados com performance dele. Nesses concursos você não podia ser muito contundente nas letras, mas na sua apresentação, Sabotage cantava uma música totalmente fora dos padrões do concurso, chamada "Na City". E a galera não acreditava que aquele moleque tinha feito a música. E foi com o grupo RZO (Rapaziada Zona Oeste),[6] que, aliás, é conhecido por revelar talentos para o público fora do rap, Negra Li, por exemplo ,[7] que Sabotage viu seu trabalho repercutir no rap nacional especialmente após a gravação de várias músicas e videoclipes, bem como a apresentação destes em shows. Na sequência,[8] Sabotage gravou seu primeiro e único disco solo, intitulado "Rap é Compromisso", gravado pelo selo Cosa Nostra, o mesmo que lançou o disco "Sobrevivendo no Inferno", dos Racionais MC's.[9][10]

O lançamento do seu primeiro álbum e as participações em shows, sobretudo nos do RZO, renderam ao rapper o convite para atuar em filmes do cinema nacional e, com isso, ter seu trabalho apreciado e reconhecido por um público ainda maior. Ao todo, foram dois os filmes em que Sabotage fez atuações: O Invasor, de Beto Brant, e Carandiru, de Héctor Babenco. Em O Invasor, Sabotage fez parte da equipe do filme, desempenhando três funções distintas. Participou da trilha sonora com cinco músicas (sendo três inéditas), serviu de consultor de "cultura da periferia" para moldar o personagem Anísio, interpretado pelo titã Paulo Miklos, e ainda por cima atuou no filme, interpretando ele mesmo, em uma cômica cena em que o personagem Anísio o apresenta para seus clientes "pedindo" um dinheiro para ele gravar seu CD. Já no filme "Carandiru", ele encarnou o personagem Fuinha e gravou uma das músicas da trilha sonora. Fez várias participações como na música "Dorobo" do BNegão; "Nem Tudo está Perdido" do Posse Mente Zulu; com Rappin' Hood; "Black Steel In the Hour of Chaos" (cover do Public Enemy) com a banda Sepultura; com Helião, Sandrão, Negra Li, Negro Útil, KL Jay em "Piri-Pac"; com Jacksom, Trilha Sonora do Gueto e Z'África Brasil em "Gíria Criminal"; e com Charlie Brown Jr. em "A Banca", "Marginal Alado" e "Cantando pro Santo".[11] Um álbum póstumo está para ser lançado em 2010.[12]
''')
    elif artista == 'beethoven':
        st.markdown('''
Ludwig van Beethoven (1770-1827) foi um compositor e pianista alemão, amplamente reconhecido como uma das figuras mais influentes da música clássica, conhecido por suas inovações e expressividade emocional.
Infância e Formação
Ludwig van Beethoven nasceu em Bonn, Alemanha, no dia 17 de dezembro de 1770. Ele era o segundo filho de Johann van Beethoven, um músico da corte, e Maria Magdalena Kepenis. Desde cedo, Beethoven foi submetido a uma rigorosa educação musical, impulsionada pelo desejo de seu pai de transformá-lo em um prodígio musical, semelhante a Mozart. Beethoven começou a estudar piano, cravo e violino, e aos 11 anos já era organista suplente da corte de Bonn. 
eBiografia

Carreira Musical
Em 1792, Beethoven mudou-se para Viena, onde estudou com Joseph Haydn e começou a construir sua carreira como compositor. Ele produziu cerca de 200 obras, incluindo sonatas, sinfonias, concertos e quartetos de cordas. Sua obra mais famosa, a Nona Sinfonia, é notável por incluir um coro no quarto movimento, uma inovação na época. 
Toda Matéria

Desafios Pessoais
Aos 27 anos, Beethoven começou a apresentar os primeiros sinais de surdez, um desafio que se agravou ao longo de sua vida. Apesar disso, ele continuou a compor algumas de suas obras mais importantes, incluindo a Missa Solene e a Décima Sinfonia, mesmo quando já estava completamente surdo. 
eBiografia

Legado
Beethoven é considerado um dos maiores compositores da história da música clássica, ao lado de Bach e Mozart. Sua música é caracterizada por uma profunda expressividade e inovação, influenciando gerações de compositores posteriores. Ele faleceu em 26 de março de 1827, em Viena, e seu túmulo se tornou um local de peregrinação para amantes da música clássica. 
Toda Matéria


A vida e a obra de Beethoven continuam a ser estudadas e celebradas, refletindo sua importância duradoura na história da música.
''')
    elif artista == 'Emilo piano':
        st.markdown('''
Emil Reinert's journey in the world of music began at a young age, with a passion for the piano that was nurtured by his family. He studied at the Hector Berlioz Conservatory and the Regional Conservatory of Paris, where he was taught by Gabriel Tacchino, the only student of Francis Poulenc. His education continued with masterclasses from renowned musicians and professors. Reinert's dedication to music led him to Hamburg, where he furthered his studies and developed his skills as a pianist. His passion for music and his ability to connect with audiences through his performances and videos have made him a global sensation.
''')
    elif artista == 'Andrea Bocelli': 
        st.markdown(''' 
Andrea Bocelli, nascido em 22 de setembro de 1958, é um renomado tenor, compositor e produtor musical italiano, conhecido por sua impressionante carreira na música clássica e popular.
Infância e Formação
Andrea Bocelli nasceu em Lajatico, na Toscana, Itália. Desde cedo, mostrou interesse pela música, começando a ter aulas de piano aos seis anos. Ele também aprendeu a tocar flauta, saxofone, trompete, harpa, violão e bateria. No entanto, sua infância foi marcada por desafios, pois nasceu com glaucoma congênito, que o deixou parcialmente cego. Aos 12 anos, um acidente durante uma partida de futebol resultou em sua cegueira total. 
Wikipedia


Após concluir o ensino médio, Bocelli ingressou na Universidade de Pisa, onde se formou em Direito. Trabalhou como advogado por um ano antes de decidir seguir sua paixão pela música, recebendo aulas de canto do renomado tenor Franco Corelli. 
Wikipedia

Carreira Musical
A carreira de Andrea Bocelli começou a ganhar destaque em 1992, quando participou de uma audição para a canção "Miserere", escrita por Zucchero e Bono do U2. Sua performance impressionou tanto que Luciano Pavarotti pediu que ele fosse escolhido para o dueto, o que catapultou Bocelli para a fama internacional. 
Wikipedia


Desde então, ele lançou vários álbuns, gravou nove óperas completas, incluindo "La bohème", "Il trovatore", "Werther" e "Tosca", e vendeu mais de 70 milhões de cópias em todo o mundo. Bocelli é reconhecido com diversos prêmios, incluindo cinco BRIT Awards e três Grammys. 
Wikipedia

Vida Pessoal
Andrea Bocelli é pai de dois filhos, Amos e Matteo. Ele foi casado com Enrica, mas atualmente está separado. Apesar de sua cegueira, Bocelli continua a se apresentar em todo o mundo, encantando o público com sua poderosa voz e emotivas performances. 
Wikipedia


A trajetória de Andrea Bocelli é um testemunho de perseverança e talento, fazendo dele uma das vozes mais amadas da música contemporânea.
''')
    else: 
        st.markdown('''
Frédéric Chopin (1810-1849) foi um compositor e pianista polonês, amplamente considerado um dos maiores compositores para piano da história.
Infância e Formação
Frédéric François Chopin nasceu em 1 de março de 1810 em Zelazowa Wola, na Polônia. Ele era filho de Nicolas Chopin, um professor francês, e de Justina Krzyżanowska, uma pianista polonesa. Desde cedo, Chopin demonstrou um talento excepcional para a música, começando a estudar piano aos seis anos e realizando seu primeiro concerto público aos oito anos. Ele se destacou no Conservatório de Varsóvia, onde estudou sob a orientação de Joseph Elsner. 
eBiografia

Carreira Musical
Em 1830, Chopin deixou Varsóvia e se estabeleceu em Viena e, posteriormente, em Paris, onde se tornou parte da elite musical da época. Ele conheceu e colaborou com outros grandes compositores, como Liszt, Berlioz e Mendelssohn. Chopin é conhecido principalmente por suas composições para piano solo, incluindo noturnos, estudos, prelúdios, baladas e sonatas. Suas obras são caracterizadas por uma profunda expressividade e uma técnica pianística inovadora, refletindo o espírito do Romantismo. 
eBiografia

Vida Pessoal
Chopin teve uma vida pessoal marcada por relacionamentos intensos, incluindo um famoso romance com a escritora George Sand. Sua saúde foi fragilizada por problemas respiratórios, que o acompanharam durante grande parte de sua vida. Ele faleceu em 17 de outubro de 1849, em Paris, e seu coração foi enterrado na Polônia, conforme seu desejo de retornar à sua terra natal. 
UOL

Legado
Chopin deixou um legado duradouro na música clássica, sendo considerado um dos maiores compositores de piano de todos os tempos. Suas obras continuam a ser amplamente executadas e admiradas em todo o mundo, e ele é frequentemente referido como o "poeta do piano" devido à beleza e à profundidade emocional de sua música. 
A mente é maravilhosa


Chopin é uma figura central na história da música, e sua influência pode ser sentida em muitos compositores que vieram depois dele. Sua música não apenas capturou a essência do Romantismo, mas também continua a ressoar com o público contemporâneo.
''')
