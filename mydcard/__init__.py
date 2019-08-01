from dcard import Dcard


def 先過濾出標題含有作品關鍵字(metas):
    return [meta for meta in metas if '' in meta['title']]


if __name__ == '__main__':

    dcard = Dcard()

    metas = dcard.forums('sex').get_metas(num=100, callback=先過濾出標題含有作品關鍵字)
    posts = dcard.posts(metas).get(comments=False, links=False)

    resources = posts.parse_resources()

    status, fails = posts.download(resources)
    print('成功下載！' if len(fails) == 0 else '出了點錯下載不完全喔')