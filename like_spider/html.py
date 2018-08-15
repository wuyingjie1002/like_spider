import re

class Html():
    """This is a class that extracts the contents of an html tag."""

    def __init__(self):
        self.tagList = []

    def setHtml(self, html = ''):
        """set the html you want to work on now"""
        if html == '':
            print('html param error')
        else:
            self.html = html
            return self

    def setTag(self, tagName = '', setAttr = {}, getAttr = (), haveFoot = True):
        """set the html tag you want to extract"""
        if tagName == '':
            print('tag param error')
        else:
            self.tagName = tagName
            self.setAttr = ''
            self.getAttr = getAttr
            if len(setAttr) > 0:
                setAttrList = []
                for attrIndex in setAttr:
                    setAttrList.append(attrIndex + '\s*=\s*[\'\"]' + setAttr[attrIndex] + '[\'\"]')
                self.setAttr = '[^>]*'.join(setAttrList)
            self.haveFoot = haveFoot
            self.tagHeadPattern = re.compile(r'<\s*'+tagName+'[^>]*>', re.S)
            self.tagFootPattern = re.compile(r'<\s*\/'+tagName+'[^>]*>', re.S)
            lastTagLen = len(self.tagList)
            if lastTagLen > 0:
                lastTagList = self.tagList
                self.tagList = []
                forCount = 0
                for lastTag in lastTagList:
                    if forCount >= lastTagLen:
                        break
                    self.html = lastTag['content']
                    self.handleTag()
                    forCount += 1
            else:
                self.handleTag()
            return self

    def handleTag(self):
        """extracted html tags"""
        if not self.haveFoot:
            pattern = re.compile(r'<\s*'+self.tagName+'[^>]*'+self.setAttr+'[^>]*>', re.S)
            headMatch = pattern.findall(self.html)
            if len(headMatch) > 0:
                for match in headMatch:
                    currTag = {'attr':{}, 'content':''}
                    if len(self.getAttr) > 0:
                        for ga in self.getAttr:
                            attrMatch = re.search(r'<\s*'+self.tagName+'[^>]*'+ga+'\s*=\s*[\'\"](.*?)[\'\"]', match, re.S)
                            if attrMatch != None:
                                currTag['attr'][ga] = attrMatch.group(1)
                    currTag['content'] = match
                    self.tagList.append(currTag)
        else:
            firstHeadMatch = re.search(r'<\s*'+self.tagName+'[^>]*'+self.setAttr+'[^>]*>', self.html, re.S)
            if firstHeadMatch != None:
                firstHead = firstHeadMatch.group()
                firstHeadLen = len(firstHead)
                firstHeadPos = self.html.find(firstHead)
                self.html = self.html[firstHeadPos:]
                footMatch = self.tagFootPattern.findall(self.html)
                if len(footMatch) > 0:
                    start = 0
                    lastStart = 0
                    end = 0
                    currHtml = ''
                    cutNum = 0
                    for index in range(len(footMatch)):
                        if index != 0 and cutNum > 0:
                            cutNum -= 1
                        if index != 0 and cutNum == 0:
                            break
                        start = self.html.find(footMatch[index], end)
                        currHtml += self.html[lastStart:start]
                        cutNum += len(self.tagHeadPattern.findall(self.html[end:start]))
                        footLen = len(footMatch[index])
                        end = start + footLen
                        lastStart = start
                        if cutNum > 1:
                            continue
                        else:
                            currHtml += self.html[start:end]
                            currTag = {'attr':{}, 'content':''}
                            if len(self.getAttr) > 0:
                                for ga in self.getAttr:
                                    attrMatch = re.search(r'<\s*'+self.tagName+'[^>]*'+ga+'\s*=\s*[\'\"](.*?)[\'\"]', currHtml, re.S)
                                    if attrMatch != None:
                                        currTag['attr'][ga] = attrMatch.group(1)
                            content = currHtml[firstHeadLen:(len(currHtml) - footLen)]
                            currTag['content'] = content
                            self.tagList.append(currTag)
                    self.html = self.html[end:]
                    self.handleTag()

    def getData(self):
        """get the extracted content"""
        tagList = self.tagList
        self.tagList = []
        return tagList
