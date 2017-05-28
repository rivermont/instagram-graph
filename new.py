
names = [
'r1vermont',
'cotton_eyed_jo',
'pickledme',
'meerkat59',
'jennifer_nelson_',
'trackstar_q21',
'matthewnelson0',
'marionphirsch',
'levithetall',
'wwestmusic',
'asherk42',
'ilove.bees',
'rorylee99',
'exorcisethebutterflies',
'ericwillie1',
'quinnolo',
'franklin_hirsch',
'subtletransformations',
'jwuliger',
'kedricscherle',
'logan_kroothoep',
'j.rudd_drummer',
'malletgirl',
'momentaryutopia',
'aaronxmoses',
'jabujam',
'zscribbleyy',
'guttermouthedhomosexual',
'kathleen.beanie',
'_bmh14',
'allykimbrough',
'orchidofthefiggs',
'dolphi_n_well',
'gratefulz',
'solomonheaden',
'liz_kimbrough',
'professional_aoife',
'vomitronx',
'bennett_place',
'_max.l_',
'aisey_king',
'jack_mcarthur',
'is_an_andy',
'ishaanr21',
'leapingleporidae',
'100_hour_benergy',
'saramic81',
'scuff934',
'breathinggalaxies',
'majorrpenny',
'yourmusic1011',
'fowlersebastian',
'alexander_bball',
'tempelouise',
'mirandastraubel',
'logicbefree',
'atticuslg',
'garrett.hudson',
'alan_reece',
'bellaz_2318',
'_ajp.123',
'the_ninja.9',
'stella.jamess',
'jenniferjbrodie',
'd7fuzz',
'elizabethfarmer',
'christi_yawn_a',
'jackson.jeffers',
'wombatz_riot',
'aidan_animallover',
'samreece_35',
'haileywunder',
'mauraholtling',
'nate.barrow',
'lynnemillies',
'roryleesullivan',
'emma5425',
'jelonster_',
'200hourbenergy',
'allykkimbrough',
'monkey_spru',
'parker.hb',
'sebcooleoh',
'thats_unusual_',
'sadierockandthemadryans',
'tempotaps',
'darkmonsterccc',
'm.iyanna',
'akidrosk3',
'salauzon',
'dani.mccrimmon',
'kaytlin.dumler',
'dae_staylit',
'ddaniel_zh',
'prisk.jaeger',
'beckett.exe',
'aceinspaaaace',
'kellymaeallen',
'thato1iverguy',
'christianna_music',
'uncovering_the_darkness',
'olivia_reece_swim',
'julia.pelle',
's.j.b.photography',
'anaxuem',
'exorcisethebutterflies.spam',
'_xxspammerxx_',
'lindsay.brand',
'smurfydoodle',
'ctrain156',
'ngraysmith',
'twig_nyland',
'gabrielle.b.m',
'tae4ducks',
'what.a.wunderful.life',
'izza.wizza',
'grier_white',
'louise_ok',
'rowaninthedeep',
'flora.1316',
'clappinghandsfarm',
'falconwarriorr',
'ribosomegirl_22',
'sebcooleoh_spam',
'blaine.the.darkone',
'fix_your_kicks',
'judananna',
'zacj0hnsen',
'brynn_holtling',
'spencer__story',
'kaitlinbunni',
'zacforvp',
'jennywarnasch',
'jayson.street',
'pennandtellerlive'
]

links = ''''''

def write(name1, names, list):
	''' str, List [str, str, ...], List [str, str, ...] -> str
	
	Returns Javascript code connections between name1 and everyone in names.
	list is a List of all names.
	
	NOTE: name1 and all contents of names must be in list.'''
	
	out = ""
	for name in names:
		out += '''\n		{source: ''' + str(list.index(name1)) + ''', target: ''' + str(list.index(name)) + '''},'''
	print(out)

def intFind(strng):
	''' str -> List
	
	Returns a list of all integers in strng.
	
	NOTE: The integers in strng must be surrounded by spaces or the function will not notice them.'''
	return [int(s) for s in strng.split() if s.isdigit()]

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def dupeCheck(data):
	mainList = (list(chunks(intFind(data), 2)))
	for a in mainList:
		a.sort()
	sorted = mainList
	done = []
	extra = []
	for b in sorted:
		if b in done:
			extra.append(b)
		done.append(b)
	return extra

dupeCheck(links)