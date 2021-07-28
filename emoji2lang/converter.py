import json
import os

class Converter:
    def __init__(self, lang = 'zh'):
        prefix = os.path.dirname(os.path.abspath(__file__))
        filename = '%s/data/%s_emoji_info.txt' % (prefix, lang)
        self.emoji_infos = {}
        for line in open(filename):
            item = json.loads(line)
            emoji = item['emoji']
            del item['emoji']
            self.emoji_infos[emoji] = item


    def convert(self, s):
        res = ''
        for ch in s:
            if ch in self.emoji_infos:
                res += '[%s]' % self.emoji_infos[ch]['简短名称']
            else:
                res += ch
        return res

    def get_emoji_infos(self, s):
        if s in self.emoji_infos:
            return self.emoji_infos[s]
        else:
            raise ValueError("no such emoji infos : %s" % s)

if __name__ == '__main__':
    converter = Converter()
    print(converter.get_emoji_infos("😀"))