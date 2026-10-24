# Balochi Word Quest — Android/Kivy test build
# Adapted from the supplied Tkinter game. Runs offline; missing sound effects are skipped.
import random, os
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Ellipse, RoundedRectangle

BALOCHI_ALPHABET = ['A', 'Á', 'B', 'CH', 'D', 'DH', 'E', 'É', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'Ó', 'P', 'R', 'S', 'SH', 'T', 'TH', 'U', 'W', 'Y', 'Z', 'ZH']

BASK_1_WORDS = ['Abad', 'Abdolláh', 'Ábád', 'Málum', 'Áshek', 'Ázom', 'Balóchi', 'Chamm', 'Dap', 'Dhann', 'Baddh', 'Badh', 'Ezgend', 'Eshk', 'Dáem', 'Érgéj', 'Yakké', 'Warnáé', 'Gósh', 'Golám', 'Hámén', 'Háji', 'Hayál', 'Imándári', 'Said', 'Dái', 'Jang', 'Kollag', 'Korbán', 'Nákon', 'Lóg', 'Molk', 'Nakanán', 'Orsond', 'Obayd', 'Óst', 'Poll', 'Parmán', 'Rang', 'Sál', 'Mirás', 'Sabr', 'Shál', 'Tap', 'Tarz', 'Thál', 'Ud', 'Nur', 'Watwáh', 'Yár', 'Niyat', 'Zend', 'Zalil', 'Zolm', 'Zedd', 'Zhand']

BASK_2_WORDS = ['Abad', 'Sar', 'Ábád', 'Sár', 'Ensán', 'Ser', 'Éraht', 'Sér', 'Imán', 'Sir', 'Ostád', 'Sor', 'Óst', 'Sór', 'Uwá', 'Sur', 'Balóchestán', 'Chamm', 'Dód', 'Dhódh', 'Gwát', 'Hár', 'Jost', 'Ketáb', 'Láp', 'Mardom', 'Nur', 'Pashk', 'Rag', 'Sáh', 'Sháh', 'Táb', 'Tháb', 'Wád', 'Yakk', 'Zend', 'Zhand', 'Chákar', 'Dhándhal', 'Shwánag', 'Thápi', 'Zhamburá', 'Zhand', 'Zhul']

BASK_3_WORDS = ['Rahshón', 'Rahband', 'Mahrang', 'Mahták', 'Sahdár', 'Shahzádag', 'Shahrag', 'Jahgir', 'Syahcháh', 'Syahgwát', 'Gonahkár', 'Behdár', 'Kohbang', 'Kas', 'Kass', 'Bas', 'Bass', 'Por', 'Porr', 'Gol', 'Goll', 'Gaz', 'Gazz', 'Kap', 'Kapp', 'Pach', 'Pacch', 'Badh', 'Baddh', 'Kash', 'Kassh', 'Bath', 'Batth', 'Bazhn', 'Bazzhag']

BASK_4_WORDS = ['Washtám', 'Zardár', 'Chamshánk', 'Kamter', 'Polgod', 'Gothgir', 'Dorgósh', 'Dozbád', 'Dozzáp', 'Garráp', 'Yakkábi', 'Tonnás', 'Yaddár', 'Yaddhawl', 'Yappád', 'Yacchamm', 'Yarrang', 'Yarráh', 'Yabbon', 'Yajjáh', 'Yakshambeh', 'Bitag', 'Bittag', 'Butag', 'Buttag', 'Diwán', 'Diwwán', 'Shum', 'Shumm', 'Din', 'Dinn', 'Zut', 'Zutt', 'Zit', 'Zitt', 'Masit', 'Masitt', 'Zirrag', 'Zirag', 'Shirr', 'Shir', 'Birr', 'Bir']

BASK_5_AW_WORDS = ['Haw', 'Taw', 'Kawr', 'Sawl', 'Gawk', 'Sawab', 'Dawr', 'Mawli', 'Hawá', 'Tawár', 'Kawár', 'Sawál', 'Gawakk', 'Sawáb', 'Dawár', 'Mawáli']

BASK_5_AY_WORDS = ['May', 'Kay', 'Say', 'Hay', 'Day', 'Gayb', 'Bay', 'Shay', 'Mayár', 'Kayl', 'Sayl', 'Hayá', 'Dayár', 'Gayáb', 'Bayán', 'Shayr', 'Ketábá', 'Koláhá', 'Molláyá', 'Barray', 'Piray', 'Kóhay', 'Man', 'Taw', 'Zhand', 'Pand', 'Hisk', 'Hampán']

GEMINATE_TO_BASE = {'CCH': 'CH', 'DDH': 'DH', 'SSH': 'SH', 'TTH': 'TH', 'ZZH': 'ZH'}


THEMES = {
    "light": {"bg":"#F4F1E9", "panel":"#FFFFFF", "panel_alt":"#FAF8F3", "ink":"#183247", "muted":"#6B7A86", "accent":"#E8A33A", "accent_hover":"#D28A22", "good":"#16836B", "bad":"#C74C4C", "line":"#E5DED1", "key":"#EEF2F4", "key_hover":"#DDE7EA", "soft":"#E8EFEF", "white":"#FFFFFF"},
    "dark": {"bg":"#101A24", "panel":"#182633", "panel_alt":"#1D2D3B", "ink":"#EDF3F6", "muted":"#A5B6C4", "accent":"#F0B454", "accent_hover":"#D99A37", "good":"#54C5A2", "bad":"#F07878", "line":"#2B3D4B", "key":"#263947", "key_hover":"#354C5C", "soft":"#223644", "white":"#FFFFFF"}
}

class BalochiWord:
    TRIGRAPHS = tuple(GEMINATE_TO_BASE.keys())
    DIGRAPHS = ("CH", "DH", "SH", "TH", "ZH")
    def __init__(self, word_text):
        self.secret = word_text.upper()
        self.tokens = self._tokenize(self.secret)
    @classmethod
    def _tokenize(cls, word):
        tokens=[]; i=0
        while i < len(word):
            c3=word[i:i+3]; c2=word[i:i+2]
            if c3 in cls.TRIGRAPHS: tokens.append(c3); i+=3
            elif c2 in cls.DIGRAPHS: tokens.append(c2); i+=2
            else: tokens.append(word[i]); i+=1
        return tokens
    @staticmethod
    def base(token): return GEMINATE_TO_BASE.get(token, token)
    def contains_guess(self, guess): return any(self.base(t)==guess.upper() for t in self.tokens)
    def revealed(self, guessed): return [t if self.base(t) in guessed else "—" for t in self.tokens]
    def hidden(self, guessed): return list(dict.fromkeys(self.base(t) for t in self.tokens if self.base(t) not in guessed))
    def solved(self, guessed): return all(self.base(t) in guessed for t in self.tokens)

class HangmanDrawing(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs); self.mistakes=0; self.bind(pos=self.draw, size=self.draw); self.draw()
    def draw(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(0.45,0.52,0.57,1); x,y=self.pos; w,h=self.size
            # centered scaffold, scales to available widget dimensions
            sx=min(w/300.0,h/285.0); ox=x+(w-300*sx)/2; oy=y+(h-285*sx)/2
            def line(points,width=3): Line(points=[ox+p[0]*sx if i%2==0 else oy+p[1]*sx for i,p in enumerate(points)], width=max(1,width*sx), cap="round")
            line([25,255,275,255],2); line([47,254,47,35],4); line([47,35,194,35],4); line([194,35,194,60],3); line([48,81,91,35],3)
            if self.mistakes>=1: Ellipse(pos=(ox+173*sx,oy+60*sx),size=(42*sx,42*sx))
            if self.mistakes>=2: line([194,102,194,166],3)
            if self.mistakes>=3: line([194,119,165,143],3)
            if self.mistakes>=4: line([194,119,223,143],3)
            if self.mistakes>=5: line([194,166,168,207],3)
            if self.mistakes>=6: line([194,166,221,207],3)

class BalochiWordQuestApp(App):
    def build(self):
        self.title="Balochi Word Quest"
        self.dark=False; self.music_on=False; self.music_volume=.15; self.bg_sound=None; self.sounds={}
        self.sound_dir=os.path.join(os.path.dirname(__file__),"sounds")
        self._load_sounds()
        self.score=0; self.streak=0; self.words_solved=0; self.words_played=0
        self.lives=6; self.max_lives=6; self.guessed=set(); self.correct=set(); self.wrong=set(); self.hint_used=False; self.round_finished=False
        self.word_bank=[]; self.bank_pos=0; self.current_word=None; self.current_lesson="Básk 3"; self.session_started=False
        self.sm=ScreenManager(transition=FadeTransition(duration=.12))
        for name in ("home","lessons","bask5","game"):
            self.sm.add_widget(Screen(name=name))
        self.show_home()
        Window.bind(on_keyboard=self._keyboard)
        return self.sm

    @property
    def t(self): return THEMES["dark" if self.dark else "light"]
    def _load_sounds(self):
        for n in ("button.mp3","correct.mp3","wrong.mp3","hint.mp3","win.mp3","lose.mp3","new_word.mp3","skip.mp3"):
            path=os.path.join(self.sound_dir,n)
            if os.path.exists(path):
                try: self.sounds[n]=SoundLoader.load(path)
                except Exception: pass
        path=os.path.join(self.sound_dir,"background.mp3")
        if os.path.exists(path):
            try:
                self.bg_sound=SoundLoader.load(path)
                if self.bg_sound: self.bg_sound.loop=True; self.bg_sound.volume=self.music_volume
            except Exception: self.bg_sound=None
    def sound(self,n):
        s=self.sounds.get(n)
        if s:
            try: s.stop(); s.play()
            except Exception: pass
    def toggle_music(self, state):
        self.music_on=bool(state)
        if self.bg_sound:
            if self.music_on:
                self.bg_sound.volume=self.music_volume
                if self.bg_sound.state!="play": self.bg_sound.play()
            else: self.bg_sound.stop()
    def set_volume(self, slider, value):
        self.music_volume=value
        if self.bg_sound: self.bg_sound.volume=value
    def C(self, hex_color):
        h=hex_color.lstrip('#'); return tuple(int(h[i:i+2],16)/255 for i in (0,2,4))+(1,)
    def label(self,text,size=14,color=None,bold=False,height=None,align='center'):
        l=Label(text=str(text),font_size=sp(size),color=self.C(color or self.t['ink']),bold=bold,halign=align,valign='middle',size_hint_y=None,height=dp(height or max(28,size*2.1)))
        l.bind(size=lambda inst,val:setattr(inst,'text_size',(val[0]-dp(8),None)))
        return l
    def button(self,text,callback,style='secondary',height=48,font_size=14):
        colors={'primary':(self.t['accent'],self.t['ink']),'secondary':(self.t['key'],self.t['ink']),'quiet':(self.t['panel_alt'],self.t['muted']),'danger':(self.t['bad'],self.t['white'])}
        bg,fg=colors[style]
        b=Button(text=text,size_hint_y=None,height=dp(height),font_size=sp(font_size),bold=True,background_normal='',background_down='',background_color=self.C(bg),color=self.C(fg))
        def action(*a): self.sound('button.mp3'); callback()
        b.bind(on_release=action)
        return b
    def card(self, orientation='vertical', padding=12, spacing=8):
        box=BoxLayout(orientation=orientation,padding=dp(padding),spacing=dp(spacing),size_hint_y=None)
        box.bind(minimum_height=box.setter('height'))
        with box.canvas.before:
            Color(*self.C(self.t['panel'])); box._bg=RoundedRectangle(pos=box.pos,size=box.size,radius=[dp(14)])
        box.bind(pos=lambda w,p:setattr(w._bg,'pos',p),size=lambda w,s:setattr(w._bg,'size',s))
        return box
    def page(self, screen_name, title, subtitle=None, back=None):
        screen=self.sm.get_screen(screen_name); screen.clear_widgets()
        root=BoxLayout(orientation='vertical',padding=dp(14),spacing=dp(10))
        root.canvas.before.clear()
        with root.canvas.before: Color(*self.C(self.t['bg'])); root._bg=RoundedRectangle(pos=root.pos,size=root.size,radius=[0])
        root.bind(pos=lambda w,p:setattr(w._bg,'pos',p),size=lambda w,s:setattr(w._bg,'size',s))
        header=BoxLayout(size_hint_y=None,height=dp(54),spacing=dp(8))
        if back: header.add_widget(self.button('‹',back,'quiet',height=44,font_size=22))
        brand=BoxLayout(orientation='vertical',spacing=0)
        brand.add_widget(self.label('BWQ  ·  BALOCHI WORD QUEST',13,self.t['ink'],True,28,'left'))
        if subtitle: brand.add_widget(self.label(subtitle.upper(),9,self.t['muted'],False,20,'left'))
        header.add_widget(brand)
        tools=BoxLayout(size_hint_x=None,width=dp(90),spacing=dp(4))
        tools.add_widget(self.button('☾' if not self.dark else '☀',self.toggle_theme,'secondary',height=42,font_size=16))
        header.add_widget(tools); root.add_widget(header)
        if title: root.add_widget(self.label(title,24,self.t['ink'],True,46))
        if screen_name in ('home','lessons','bask5','game'):
            audio=BoxLayout(size_hint_y=None,height=dp(38),spacing=dp(8))
            audio.add_widget(self.label('Music',10,self.t['muted'],True,28))
            sw=Switch(active=self.music_on,size_hint_x=None,width=dp(48)); sw.bind(active=lambda inst,val:self.toggle_music(val)); audio.add_widget(sw)
            audio.add_widget(self.label('Vol',10,self.t['muted'],True,28))
            sl=Slider(min=0,max=1,value=self.music_volume); sl.bind(value=self.set_volume); audio.add_widget(sl)
            root.add_widget(audio)
        screen.add_widget(root)
        return root
    def body_scroll(self, root):
        scroll=ScrollView(do_scroll_x=False,bar_width=dp(3))
        content=BoxLayout(orientation='vertical',padding=(dp(3),dp(4)),spacing=dp(12),size_hint_y=None)
        content.bind(minimum_height=content.setter('height')); scroll.add_widget(content); root.add_widget(scroll)
        return content
    def show_home(self):
        root=self.page('home',None,'Learn a word. Keep the language alive.')
        body=self.body_scroll(root)
        hero=self.card(padding=18,spacing=12); body.add_widget(hero)
        hero.add_widget(self.label('Learn a word.\nKeep the language alive.',28,self.t['ink'],True,94))
        hero.add_widget(self.label('A Balochi vocabulary guessing game with all five Básk lessons. Guess the alphabet tokens, protect your lives, and build your streak.',13,self.t['muted'],False,78))
        for n,title,desc in [('01','BALOCHI TOKENS','Includes CH, DH, SH, TH and ZH.'),('02','SMART HINT','Reveal one hidden token at a life cost.'),('03','STREAK BONUS','Keep solving words to grow your score.')]:
            tile=self.card(padding=10,spacing=3); tile.add_widget(self.label(n+'  ·  '+title,12,self.t['accent'],True,26)); tile.add_widget(self.label(desc,11,self.t['muted'],False,35)); hero.add_widget(tile)
        hero.add_widget(self.button('Resume Game' if self.session_started else 'Start Playing',self.show_lessons,'primary',52,16))
        hero.add_widget(self.button('How to Play',self.show_rules,'secondary'))
        hero.add_widget(self.label('OFFLINE WORD GAME  ·  TEST BUILD',9,self.t['muted'],False,24))
        self.sm.current='home'
    def show_rules(self):
        text='1. Choose a Balochi token from the keyboard.\n\n2. Each incorrect guess removes one life. You start with six lives.\n\n3. A hint reveals one hidden token and costs one life. One hint per word.\n\n4. Solve a word to earn 10 points plus 2 for each remaining life. Every third consecutive solve earns a 5-point streak bonus.\n\n5. CH, DH, SH, TH and ZH are single tokens. Doubled forms reveal with their base digraph.'
        p=Popup(title='How to Play',content=self.label(text,14,self.t['ink'],False,300),size_hint=(.9,.8)); p.open()
    def show_lessons(self):
        root=self.page('lessons','Choose a Lesson','Select the Básk section you want to practise.',self.show_home); body=self.body_scroll(root)
        options=[('Básk 1 · Alphabet',BASK_1_WORDS,'Básk 1'),('Básk 2 · Vowels & consonants',BASK_2_WORDS,'Básk 2'),('Básk 3 · Long vowels & doubled forms',BASK_3_WORDS,'Básk 3'),('Básk 4 · Doubled letters & word blends',BASK_4_WORDS,'Básk 4')]
        for title,words,name in options: body.add_widget(self.button(title,lambda w=words,n=name:self.start_lesson(w,n),'primary',54,14))
        body.add_widget(self.button('Básk 5 · Aw / Ay & hamza',self.show_bask5,'primary',54,14)); body.add_widget(self.button('Back to Home',self.show_home,'secondary'))
        self.sm.current='lessons'
    def show_bask5(self):
        root=self.page('bask5','Básk 5','Choose a section to practise.',self.show_lessons); body=self.body_scroll(root)
        body.add_widget(self.button('Aw',lambda:self.start_lesson(BASK_5_AW_WORDS,'Básk 5 — Aw'),'primary',56,16))
        body.add_widget(self.button('Ay + Hamza examples',lambda:self.start_lesson(BASK_5_AY_WORDS,'Básk 5 — Ay / Hamza'),'primary',56,16))
        body.add_widget(self.button('Back to lessons',self.show_lessons,'secondary'))
        self.sm.current='bask5'
    def start_lesson(self,words,name):
        self.current_lesson=name; self.word_bank=list(words); random.shuffle(self.word_bank); self.bank_pos=0
        self.score=0; self.streak=0; self.words_solved=0; self.words_played=0; self.session_started=True
        self.load_word(); self.show_game()
    def load_word(self):
        if not self.word_bank: return
        if self.bank_pos>=len(self.word_bank): random.shuffle(self.word_bank); self.bank_pos=0
        self.current_word=BalochiWord(self.word_bank[self.bank_pos]); self.bank_pos+=1
        self.guessed=set(); self.correct=set(); self.wrong=set(); self.lives=6; self.hint_used=False; self.round_finished=False
        self.status='Choose a token to begin.'; self.status_kind='neutral'; self.round_score_before=self.score; self.round_points=0
    def show_game(self):
        root=self.page('game',None,self.current_lesson,self.show_lessons); body=self.body_scroll(root)
        stats=GridLayout(cols=3,spacing=dp(6),size_hint_y=None,height=dp(74))
        for label,value in [('TOTAL SCORE',self.score),('STREAK',self.streak),('WORDS SOLVED',f'{self.words_solved}/{self.words_played}')]:
            c=self.card(padding=5,spacing=2); c.add_widget(self.label(label,9,self.t['muted'],True,22)); c.add_widget(self.label(value,17,self.t['good'] if label=='TOTAL SCORE' else self.t['ink'],True,30)); stats.add_widget(c)
        body.add_widget(stats)
        challenge=self.card(padding=12,spacing=5); body.add_widget(challenge)
        challenge.add_widget(self.label('THE CHALLENGE',10,self.t['muted'],True,22)); challenge.add_widget(self.label('Protect your six lives',16,self.t['ink'],True,30)); challenge.add_widget(self.label(f'LIVES LEFT  {self.lives}/6     WORD BANK  {self.bank_pos:02d}/{len(self.word_bank):02d}',11,self.t['muted'],True,26))
        self.drawing=HangmanDrawing(size_hint_y=None,height=dp(190)); challenge.add_widget(self.drawing)
        puzzle=self.card(padding=12,spacing=8); body.add_widget(puzzle)
        puzzle.add_widget(self.label('GUESS THE WORD',10,self.t['muted'],True,22))
        self.word_label=self.label('   '.join(self.current_word.revealed(self.guessed)),25,self.t['ink'],True,60); puzzle.add_widget(self.word_label)
        self.status_label=self.label(self.status,12,self.t['muted'],False,42); puzzle.add_widget(self.status_label)
        self.keys=GridLayout(cols=5,spacing=dp(5),size_hint_y=None); self.keys.bind(minimum_height=self.keys.setter('height'))
        for token in BALOCHI_ALPHABET:
            b=Button(text=token,size_hint_y=None,height=dp(43),font_size=sp(13),bold=True,background_normal='',background_color=self.C(self.t['key']),color=self.C(self.t['ink']))
            b.bind(on_release=lambda inst,t=token:self.make_guess(t)); self.keys.add_widget(b)
        puzzle.add_widget(self.keys)
        actions=GridLayout(cols=2,spacing=dp(8),size_hint_y=None,height=dp(100))
        actions.add_widget(self.button('Reveal a token · costs 1 life',self.use_hint,'primary',48,12))
        actions.add_widget(self.button('Next word',self.next_word,'secondary',48,12))
        actions.add_widget(self.button('New lesson',self.show_lessons,'quiet',42,12))
        actions.add_widget(self.button('Home',self.show_home,'quiet',42,12))
        puzzle.add_widget(actions)
        self.sm.current='game'; self.refresh_game()
    def refresh_game(self):
        if not hasattr(self,'word_label') or not self.current_word: return
        shown=self.current_word.revealed(self.guessed)
        if self.round_finished and not self.current_word.solved(self.guessed): shown=self.current_word.tokens
        self.word_label.text='   '.join(shown)
        self.word_label.color=self.C(self.t['good'] if self.round_finished and self.current_word.solved(self.guessed) else self.t['bad'] if self.round_finished else self.t['ink'])
        self.status_label.text=self.status; self.status_label.color=self.C({'good':self.t['good'],'bad':self.t['bad'],'warning':self.t['accent'],'neutral':self.t['muted']}.get(self.status_kind,self.t['muted']))
        self.drawing.mistakes=6-self.lives; self.drawing.draw()
        for b in self.keys.children:
            token=b.text
            if token in self.guessed:
                b.background_color=self.C(self.t['good'] if token in self.correct else self.t['bad']); b.color=self.C(self.t['white']); b.disabled=True
            else:
                b.background_color=self.C(self.t['key']); b.color=self.C(self.t['ink']); b.disabled=self.round_finished
    def make_guess(self,token):
        if not self.current_word or self.round_finished or token in self.guessed:return
        self.guessed.add(token)
        if self.current_word.contains_guess(token):
            self.correct.add(token); self.status=f'Good guess — {token} is in the word.'; self.status_kind='good'; self.sound('correct.mp3')
        else:
            self.wrong.add(token); self.lives-=1; self.status=f'{token} is not in the word. {self.lives} lives left.'; self.status_kind='bad'; self.sound('wrong.mp3')
        self.check_end(); self.refresh_game()
    def use_hint(self):
        if self.round_finished or self.hint_used:return
        if self.lives<=1: self.status='Keep at least two lives to use a hint.'; self.status_kind='warning'; self.refresh_game(); return
        hidden=self.current_word.hidden(self.guessed)
        if not hidden:return
        token=random.choice(hidden); self.guessed.add(token); self.correct.add(token); self.lives-=1; self.hint_used=True
        self.status=f'Hint used: {token} revealed. One life spent.'; self.status_kind='warning'; self.sound('hint.mp3'); self.check_end(); self.refresh_game()
    def check_end(self):
        if self.current_word.solved(self.guessed):
            self.round_finished=True; self.words_solved+=1; self.words_played+=1; self.streak+=1
            self.round_points=10+self.lives*2+(5 if self.streak%3==0 else 0); self.score+=self.round_points; self.status='Excellent! Word completed.'; self.status_kind='good'; self.sound('win.mp3'); self.show_result(True)
        elif self.lives<=0:
            self.round_finished=True; self.words_played+=1; self.streak=0; self.status='Out of lives — keep learning!'; self.status_kind='bad'; self.sound('lose.mp3'); self.show_result(False)
    def show_result(self,won):
        text=f"The word was: {self.current_word.secret}\nPoints earned: +{self.round_points if won else 0}\nTotal score: {self.score}"
        box=BoxLayout(orientation='vertical',padding=dp(14),spacing=dp(10)); box.add_widget(self.label(('Excellent! Word completed!' if won else 'Out of lives — keep learning!'),17,self.t['good'] if won else self.t['bad'],True,42)); box.add_widget(self.label(text,14,self.t['ink'],True,72))
        row=GridLayout(cols=3,spacing=dp(6),size_hint_y=None,height=dp(48))
        row.add_widget(self.button('Retry',self.retry_word,'secondary',44,12)); row.add_widget(self.button('Skip',self.skip_word,'primary',44,12)); row.add_widget(self.button('New',self.new_lesson,'secondary',44,12)); box.add_widget(row)
        self.result_popup=Popup(title='Word complete' if won else 'Try again',content=box,size_hint=(.9,None),height=dp(300),auto_dismiss=False); self.result_popup.open()
    def close_result(self):
        if getattr(self,'result_popup',None): self.result_popup.dismiss(); self.result_popup=None
    def retry_word(self):
        self.close_result(); self.current_word=BalochiWord(self.current_word.secret.title()); self.guessed=set(); self.correct=set(); self.wrong=set(); self.lives=6; self.hint_used=False; self.round_finished=False; self.status='Try the word again.'; self.status_kind='neutral'; self.show_game()
    def skip_word(self):
        self.close_result(); self.sound('skip.mp3'); self.load_word(); self.show_game()
    def new_lesson(self):
        self.close_result(); self.sound('new_word.mp3'); words=self.word_bank; name=self.current_lesson; self.start_lesson(words,name)
    def next_word(self):
        if not self.round_finished:return
        self.sound('new_word.mp3'); self.load_word(); self.show_game()
    def toggle_theme(self):
        self.dark=not self.dark
        cur=self.sm.current
        if cur=='home': self.show_home()
        elif cur=='lessons': self.show_lessons()
        elif cur=='bask5': self.show_bask5()
        elif cur=='game': self.show_game()
    def _keyboard(self,window,key,scancode,codepoint,modifiers):
        if codepoint:
            token=codepoint.upper()
            if token in BALOCHI_ALPHABET and self.sm.current=='game': self.make_guess(token)
        return False

if __name__=='__main__': BalochiWordQuestApp().run()
