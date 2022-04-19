# -*- coding: utf-8 -*-

import pytest
import datetime
import irc_parse



def test_sanity():
    assert irc_parse.sanity_check() == True


# some sample rows
# data
# comments in chat
comment_row_1 = '01:17 < HeavenGuard> hello?\n' 
comment_row_2 = '19:29 <+Cogitabundus> Some like chaos.\n'
comment_row_3 = '19:29 <%Cogit1234> Some like chaos.\n'
comment_row_4 = '19:29 <~leeroy> Some like < User1234>. It is 12:34 \n'
comment_row_5 = '20:06 < gucci|bebe> anybody have any tips?\n'
comment_row_6 = '16:14 < Backbox[]> Still going over the tv thing?\n'
comment_row_7 = '19:55 < {L}> hope its now good\n'
comment_row_8 = '02:45 < \\2h1s> just lol\n'
comment_row_9 = '20:57 < `\\> zid swetchun teh lettaz ap!\n'

# join/quit messages (those that start with -!-)
info_row_1 = '00:01 -!- Guest40341 [AndChat2541@AN-pl0gl1.8e2d.64f9.r226rd.IP] has quit [Quit: Bye]'
info_row_2 = '18:39 -!- Hex [Hex@Quantum.Time] has quit [ < Hex> ]'
info_row_3 = '00:15 -!- _CyBruh_ [-Cybruh@AN-gm6.oj9.rj1tv4.IP] has quit [Quit: Leaving]' 
info_row_4 = '04:38 -!- gucci|bebe [guccibebe@errrrthang.guc.ci] has joined #hackers'
info_row_5 = '10:06 -!- Whiskey-Tango-Down [Whiskey-Tan@she.wuz.ded.already.piig] has joined #hackers'
info_row_6 = '10:49 -!- azorean [Mr.NoOne@AN-tga.mto.vlu2el.IP] has joined #hackers'
info_row_7 = '13:43 -!- V`ger [V`ger@AN-4i0.ekd.20rmgn.IP] has joined #hackers'
info_row_8 = '19:09 -!- Backbox[] [Backbox[]@AN-rcj.sk0.r02qji.IP] has joined #hackers'
info_row_9 = '10:10 -!- Pysis|work [Pysis|work@AN-942.7r1.h4t911.IP] has joined #hackers'
info_row_10 = '21:42 -!- ajah^ [ajah^@AN-tsm.ti5.74h9kl.IP] has joined #hackers'
info_row_11 = '05:25 -!- Laris [undead@2a07:9944:10::1fc:4f1e] has joined #hackers'
info_row_12 = '17:59 -!- _{DaRk0VeNoM}_ [_{DaRk0VeNo@AN-f0s.24t.r8c6uv.IP] has joined #hackers'
info_row_13 = '14:37 -!- \\2h1s [\\21hs@AN-v15.cca.e529l0.IP] has joined #hackers'
info_row_14 = '00:44 -!- SiliconAlchemist [anon@technoalchemy.com] has left #hackers []'

name_change_1 = '01:31 -!- hellboy is now known as Guest26312'
name_change_2 = "21:22 -!- You're now known as Giratina"

mode_change_1 = '12:48 -!- mode/#hackers [+h guapo] by EmmaWatson'
mode_change_2 = '15:20 -!- ServerMode/#hackers [+qovaov evilbox evilbox Meow EmmaWatson EmmaWatson Cogitabundus] by AnonOps'

sync_row_1 = '21:22 -!- Irssi: #hackers: Total of 65 nicks [4 ops, 1 halfops, 3 voices, 57 normal]'
sync_row_2 = '21:23 -!- Irssi: Join to #hackers was synced in 60 secs'

# log open/date changed (rows starting with ---)
log_open_1 = '--- Log opened Tue Sep 20 00:01:49 2016'
log_open_2 = '--- Day changed Sun Apr 29 2018'

# emote rows
emote_1 = '08:23  * eezee is now playing: Smash Mouth - All Star\n'

# topic rows
topic_1 = '00:00 -EmmaWatson:#hackers- Channel Topic: No carding, schools, facebook - Use -tools for info and -nameoftool for more info - USE A FUCKING VPN - Other chans: #tutorials #ddos Support arrested anons http://goo.gl/Bz92ES | Hacking aid https://google.com | LURK MOAR\n'
topic_2 = '05:24 -!- Iggy changed the topic of #hackers to: No carding, no .edu *NO FB*- Use -tools for info and -nameoftool for more info - USE A FUCKING VPN - Other chans: #tutorials #ddos Support arrested anons http://goo.gl/Bz92ES | Hacking aid https://google.com | LURK MOAR | satan eats dicks*'



@pytest.mark.parametrize('row,expected', [(comment_row_1, ' '), 
                                          (comment_row_2, '+'),
                                          (comment_row_3, '%'),
                                          (comment_row_4, '~'),
                                          (comment_row_5, ' '),
                                          (comment_row_6, ' '),
                                          (comment_row_7, ' '),
                                          (comment_row_8, ' '),
                                          (comment_row_9, ' ')])
def test_get_admin_flag(row, expected):
    assert irc_parse.get_admin_flag(row) == expected


def test_find_urls():
    # Test 1 - A single URL as input
    case_1_input = 'https://www.github.com/'
    case_1_output = ["https://www.github.com/"]
    assert irc_parse.find_urls(case_1_input) == case_1_output

    # Test 2 - longer URLs
    case_2_input = "https://www.github.com/lspitzley/bfor206_spring2022"
    case_2_output = ["https://www.github.com/lspitzley/bfor206_spring2022"]
    assert irc_parse.find_urls(case_2_input) == case_2_output

    # Test 3 - no URLs
    case_3_input = "There are no URLs in this string"
    case_3_output = []
    assert irc_parse.find_urls(case_3_input) == case_3_output

    # Test 4 - multiple URLs
    case_4_input = "I like https://github.com, I also like https://bitbucket.com/"
    case_4_output = ["https://github.com,", "https://bitbucket.com/"]
    assert irc_parse.find_urls(case_4_input) == case_4_output

    # Test 5 - numpy nan value as input
    import numpy as np
    case_5_input = np.nan
    case_5_output = []
    assert irc_parse.find_urls(case_5_input) == case_5_output

@pytest.mark.parametrize('row,expected', [(log_open_1, datetime.datetime(2016, 9, 20)),
                                          (log_open_2, datetime.datetime(2018, 4, 29))])
def test_get_current_date(row, expected):
    assert irc_parse.get_current_date(row) == expected



@pytest.mark.parametrize('row,expected', [(comment_row_1, {'hour': 1,  'minute': 17}), 
                                          (comment_row_2, {'hour': 19, 'minute': 29}),
                                          (comment_row_3, {'hour': 19, 'minute': 29}),
                                          (comment_row_4, {'hour': 19, 'minute': 29}),
                                          (info_row_1,    {'hour': 0,  'minute': 1 }),
                                          (log_open_1,    {})])
def test_get_hours_minutes(row, expected):
    assert irc_parse.get_hours_minutes(row) == expected



@pytest.mark.parametrize('row,expected', [(info_row_1, 'Guest40341'),
                                          (info_row_2, 'Hex'),
                                          (info_row_3, '_CyBruh_'),
                                          (info_row_4, 'gucci|bebe'),
                                          (info_row_5, 'Whiskey-Tango-Down'),
                                          (info_row_6, 'azorean'),
                                          (info_row_7, 'V`ger'),
                                          (info_row_8, 'Backbox[]'),
                                          (info_row_9, 'Pysis|work'),
                                          (info_row_10, 'ajah^'),
                                          (info_row_11, 'Laris'),
                                          (info_row_12, '_{DaRk0VeNoM}_'),
                                          (info_row_13, '\\2h1s'),
                                          (info_row_14, 'SiliconAlchemist')])
def test_get_join_quit_username(row, expected):
    assert irc_parse.get_join_quit_username(row) == expected





@pytest.mark.parametrize('row,expected', [(comment_row_1, False), 
                                          (comment_row_2, False),
                                          (comment_row_3, False),
                                          (comment_row_4, False),
                                          (info_row_1, False),
                                          (info_row_2, False),
                                          (info_row_3, False),
                                          (info_row_4, False),
                                          (info_row_5, False),
                                          (info_row_6, False),
                                          (log_open_1, True),
                                          (log_open_2, True)])
def test_is_date_row(row, expected):
    assert irc_parse.is_date_row(row) == expected


@pytest.mark.parametrize('row,expected', [(comment_row_1, False), 
                                          (comment_row_2, False),
                                          (comment_row_3, False),
                                          (comment_row_4, False),
                                          (info_row_1, True),
                                          (info_row_2, True),
                                          (info_row_3, True),
                                          (info_row_4, True),
                                          (info_row_5, True),
                                          (info_row_6, True),
                                          (info_row_7, True),
                                          (info_row_8, True),
                                          (info_row_9, True),
                                          (info_row_10, True),
                                          (info_row_11, True),
                                          (info_row_12, True),
                                          (info_row_13, True),
                                          (info_row_14, True),
                                          (log_open_1, False)])
def test_is_join_quit(row, expected):
    assert irc_parse.is_join_quit(row) == expected

@pytest.mark.parametrize('row,expected', [(comment_row_1, True), 
                                          (comment_row_2, True),
                                          (comment_row_3, True),
                                          (comment_row_4, True),
                                          (comment_row_5, True),
                                          (comment_row_6, True),
                                          (comment_row_7, True),
                                          (comment_row_8, True),
                                          (comment_row_9, True),
                                          (info_row_1, False),
                                          (info_row_2, False),
                                          (log_open_1, False)])
def test_is_message(row, expected):
    assert irc_parse.is_message(row) == expected
    
    






@pytest.mark.parametrize('row,expected', [(comment_row_1, False), 
                                          (comment_row_2, False),
                                          (comment_row_3, False),
                                          (comment_row_4, False),
                                          (info_row_1, False),
                                          (info_row_2, False),
                                          (info_row_3, False),
                                          (info_row_4, False),
                                          (info_row_5, False),
                                          (info_row_6, False),
                                          (log_open_1, False),
                                          (emote_1, True)])
def test_is_emote(row, expected):
    assert irc_parse.is_emote(row) == expected


@pytest.mark.parametrize('row,expected', [(topic_1, True),
                                          (topic_2, True)])
def test_is_topic(row, expected):
    assert irc_parse.is_topic(row) == expected


@pytest.mark.parametrize('row, expected', [(comment_row_1, 'HeavenGuard'),
                                           (comment_row_2, 'Cogitabundus'),
                                           (comment_row_3, 'Cogit1234'),
                                           (comment_row_4, 'leeroy'),
                                           (comment_row_5, 'gucci|bebe'),
                                           (comment_row_6, 'Backbox[]'),
                                           (comment_row_7, '{L}'),
                                           (comment_row_8, '\\2h1s'),
                                           (comment_row_9, '`\\'),])
def test_get_user_name(row, expected):
    assert irc_parse.get_user_name(row) == expected


@pytest.mark.parametrize('row, expected', [(comment_row_1, None),
                                           (comment_row_2, '+'),
                                           (comment_row_3, '%'),
                                           (comment_row_4, '~'),
                                           (comment_row_5, None),
                                           (comment_row_6, None),
                                           (comment_row_7, None),
                                           (comment_row_8, None),
                                           (comment_row_9, None),])
def test_get_user_prefix(row, expected):
    assert irc_parse.get_user_prefix(row) == expected


@pytest.mark.parametrize('row, expected', [(comment_row_1, 'hello?\n'),
                                           (comment_row_2, 'Some like chaos.\n'),
                                           (comment_row_3, 'Some like chaos.\n'),
                                           (comment_row_4, 'Some like < User1234>. It is 12:34 \n'),
                                           (comment_row_5, 'anybody have any tips?\n'),
                                           (comment_row_6, 'Still going over the tv thing?\n'),
                                           (comment_row_7, 'hope its now good\n'),
                                           (comment_row_8, 'just lol\n'),
                                           (comment_row_9, 'zid swetchun teh lettaz ap!\n'),])
def test_get_chat_message(row, expected):
    assert irc_parse.get_chat_message(row) == expected
