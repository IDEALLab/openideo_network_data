import datetime
import networkx as nx

class Comment(object):
    ''' Defines a particular comment and any sub-comments on an idea '''
    def __init__(self,node_id,user,user_url,date,text,applause=0,sub_comments = []):
        self.node = node_id   # which node_id this comment is about
        self.user = user    # which user wrote it
        self.user_url = user_url    # what's the users url
        self.date = date    # When was it written
        self.text = text    # What was the comment
        self.applause = applause    # How much applause did the comment get
        self.sub_comments = sub_comments    # Any sub-comments in reply?

    def add_sub_comment(self,new_comment):
        self.sub_comments.append(new_comment)

class Node(object):

    def __init__(self, title, type_of, node_id, description, firstname,
                  lastname, creator, created, image, basedon, children=None,
                  url=None, text_body = None, applause=0,views =0,
                  winner=False,comment_count =0,comments = [],evaluations=[],
                  calculated_evaluations={},themes=[]):
        self.title = title
        self.type_of = type_of
        self.node_id = node_id
        self.description = description
        self.firstname = firstname
        self.lastname = lastname
        self.creator = creator
        self.created = created
        self.image = image
        self.basedon = basedon
        self.children = children
        self.url = url
        self.text_body = text_body
        self.applause = applause
        self.views = views
        self.winner = winner
        self.comment_count = comment_count
        self.comments = comments
        self.evaluations = evaluations
        self.calculated_evaluations = calculated_evaluations
        self.themes=themes

    def add_comment(new_comment):
        self.comments.append(new_comment)

class User(object):
    def __init__(self, name, design_quotient={}, occupation=None, company=None):
        self.name = name
        self.design_quotient = design_quotient
        self.occupation = occupation
        self.company = company

class Challenge(object):
    '''Data structure for handling everything related to a given challenge'''
    def __init__(self,number, link, title, description, sponsor=None,start_date=None, end_date=None):
        self.number = number
        self.link = link
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.sponsor = sponsor
        self.concept_graph = nx.DiGraph()
        self.social_graph = nx.DiGraph()
