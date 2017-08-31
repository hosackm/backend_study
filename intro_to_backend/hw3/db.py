import sqlite3
import datetime
from collections import namedtuple

Post = namedtuple("Post", ("id", "title", "content", "created_date"))


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(":memory:", check_same_thread=False)
        self.create_database()

    def create_database(self):
        self.connection.execute(
            "CREATE TABLE posts (id integer PRIMARY KEY, title text, content text, created_date date)")
        for p in fake_posts:
            self.add_post(p.title, p.content)

    def get_post_by_id(self, id):
        cur = self.connection.execute("SELECT * FROM posts WHERE id == ?", (id,))
        post = cur.fetchone()
        if post:
            post = Post(*post)
            return {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "date": post.created_date.split()[0]
            }
        return {}

    def get_most_recent_posts(self, n=10):
        cur = self.connection.execute("SELECT * FROM posts ORDER BY created_date DESC")
        posts = [Post(*c) for c in cur.fetchmany(n)]
        return posts[:n]

    def add_post(self, title, content):
        created_date = datetime.datetime.today()
        cur = self.connection.execute(
            "INSERT INTO posts(title, content, created_date) VALUES (?, ?, ?)", (title, content, created_date))

        print("added post:", cur.lastrowid)
        return cur.lastrowid


lorem_ipsum = """
Vaporware kitsch austin blog fam. Pug before they sold out quinoa meggings, chartreuse marfa fingerstache disrupt
distillery master cleanse. Vegan organic godard photo booth pour-over direct trade hashtag snackwave biodiesel
typewriter cornhole meditation humblebrag. Squid shaman salvia franzen migas art party, shoreditch beard leggings.
Live-edge put a bird on it iceland hot chicken. Ennui succulents hexagon everyday carry mumblecore, deep v biodiesel
flexitarian man bun pug sustainable scenester. Mumblecore chia waistcoat vinyl tousled pitchfork. Waistcoat etsy
normcore man braid twee. Meh messenger bag banjo etsy. Intelligentsia knausgaard yuccie iceland. Migas brunch sartorial
dreamcatcher pinterest, man bun messenger bag pug cardigan tumblr helvetica pitchfork lyft activated charcoal gochujang.

Bushwick hell of semiotics, poutine kombucha venmo banjo activated charcoal kitsch. Tbh vexillologist mlkshk 90's
narwhal echo park intelligentsia palo santo forage hoodie cardigan tousled. Fanny pack crucifix tousled, portland
readymade locavore viral edison bulb succulents. Keffiyeh subway tile helvetica, pug distillery tacos craft beer.
Hella literally DIY adaptogen, ramps poke venmo yr. Disrupt before they sold out celiac, asymmetrical pinterest kogi
squid sriracha vexillologist. Drinking vinegar glossier chillwave mixtape lomo, farm-to-table 90's narwhal tumblr
live-edge. Skateboard kombucha raw denim, ethical thundercats messenger bag truffaut williamsburg succulents meggings
letterpress. Literally occupy taxidermy shaman air plant vaporware dreamcatcher narwhal palo santo DIY. Cred jianbing
viral crucifix squid master cleanse. Woke live-edge tacos slow-carb. Shaman pabst distillery ethical.

Lumbersexual live-edge keytar tumeric vexillologist, microdosing copper mug listicle organic vape pug man bun mixtape.
Food truck whatever sartorial tumeric enamel pin sustainable everyday carry vegan salvia. Meditation microdosing beard
hella narwhal viral prism chicharrones franzen master cleanse hammock lomo skateboard tilde. Bitters gochujang cred
sartorial actually, pour-over truffaut fam neutra yuccie. Coloring book paleo cliche literally. Woke shaman cliche
squid small batch glossier prism seitan. Normcore banjo poutine, vape VHS trust fund squid truffaut echo park locavore
sriracha live-edge chicharrones beard biodiesel. Freegan cloud bread keffiyeh fashion axe church-key ethical 3 wolf
moon. Flexitarian wayfarers thundercats blog synth 8-bit vegan fingerstache crucifix four dollar toast. Locavore twee
austin kombucha, farm-to-table poke brooklyn tilde flexitarian pabst four dollar toast. Marfa YOLO VHS, humblebrag
bitters +1 letterpress. Vape enamel pin cray celiac vegan semiotics succulents schlitz. Crucifix palo santo freegan
fanny pack cold-pressed four loko authentic tilde asymmetrical shaman tbh mixtape intelligentsia. Slow-carb tote bag
succulents fashion axe hot chicken brunch four dollar toast yuccie etsy everyday carry tbh green juice. Quinoa franzen
dreamcatcher bushwick ramps raw denim whatever.

Tbh tumblr whatever deep v raclette gochujang. Heirloom humblebrag readymade, polaroid subway tile whatever tote bag
90's blog vexillologist aesthetic tofu. Vinyl pitchfork letterpress try-hard bushwick humblebrag cold-pressed
intelligentsia tote bag bicycle rights pop-up flannel crucifix selfies health goth. Everyday carry vape literally
normcore kickstarter. Waistcoat migas tacos plaid chicharrones heirloom cronut vaporware slow-carb portland. Craft
beer occupy williamsburg, waistcoat truffaut tote bag distillery post-ironic. Man braid snackwave meggings listicle
twee fixie stumptown chicharrones. Truffaut forage sartorial, hot chicken jean shorts neutra kickstarter lumbersexual
wayfarers chia air plant edison bulb. Jean shorts vinyl organic raw denim 90's celiac. Copper mug poke pok pok
knausgaard hammock. Vexillologist jianbing fashion axe tumblr godard four loko kombucha flannel vaporware. Readymade
pour-over normcore banjo.

Keffiyeh dreamcatcher austin iPhone. Organic cronut green juice, cred succulents keffiyeh scenester man braid
gluten-free distillery gastropub. +1 master cleanse literally 90's blog, iPhone seitan pabst health goth mlkshk
man bun gochujang 8-bit tacos. Bitters yuccie ugh meggings master cleanse post-ironic lyft fanny pack mustache VHS
kale chips PBR&B cornhole. Actually iceland bespoke, shaman man bun try-hard chia fingerstache offal truffaut sartorial
slow-carb. Glossier pok pok coloring book brunch +1 keytar gluten-free af wolf hella messenger bag organic. Literally
meditation gentrify, paleo microdosing farm-to-table heirloom vinyl vape synth biodiesel pickled organic. Drinking
vinegar man braid cloud bread tofu VHS. Letterpress migas literally tofu everyday carry, bushwick occupy taxidermy
seitan banh mi. Organic artisan kitsch, everyday carry bushwick bespoke roof party affogato plaid ethical live-edge
celiac 90's offal. Biodiesel DIY taxidermy, trust fund paleo brooklyn edison bulb fixie jean shorts air plant try-hard
church-key 90's. Cliche before they sold out helvetica banh mi portland kitsch.

Oh. You need a little dummy text for your mockup? How quaint.

I bet you're still using Bootstrap too
"""
fake_date = datetime.datetime.today()
fake_posts = [Post(n, "Title {}".format(n), lorem_ipsum, fake_date) for n in range(1, 50)]
db = Database()

if __name__ == "__main__":
    print(db.get_post_by_id(1))
    id = db.add_post("Blargh!", "ERMAGHERD!")
    print(db.get_post_by_id(id))
    for i, post in enumerate(db.get_most_recent_posts(), 1):
        print(i, post.title)
