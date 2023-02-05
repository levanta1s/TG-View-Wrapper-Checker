
import time
import pyrogram
from datetime import datetime
from config import api_hash,api_id,channel_id,delay,trigger_count,range

app = pyrogram.Client("my_account",api_id,api_hash)
app.start()


posts = app.get_chat_history(channel_id)
post_views = {}
for post in posts:
    post_views[post.id] = post.views

while True:
    try:
        time.sleep(delay)
        new_posts = app.get_chat_history(channel_id)
        counter = 0
        for post in new_posts:
            if counter != range:
                if post.id in post_views:
                    try:
                        views_diff = post.views - post_views[post.id]
                        if views_diff >= trigger_count:
                            app.delete_messages(chat_id=channel_id, message_ids=post.id)
                            print(f'[DELETED] {str(datetime.now().time())[:5]} | ID - {post.id} | Количество просмотров: {post.views}')
                    except:
                        pass
                else:
                    post_views[post.id] = post.views
            else:
                break
            counter +=1
    except:
        pass



