openideo_network_data
=====================

Raw data files for several research experiments that use OI design network data. If you use this data in any of your own research, please cite the following articles:

Mark Fuge, Kevn Tee, Alice Agogino, and Nathan Maton
Analysis of Collaborative Design Networks: A Case Study of OpenIDEO
Journal of Computing and Information Science in Engineering, 14(2) :021009+
(2014, March) 
    
    @article{fuge:openideo_JCISE_2014,
        author = {Fuge, Mark and Tee, Kevin and Agogino, Alice and Maton, Nathan},
        doi = {10.1115/1.4026510},
        issn = {1530-9827},
        journal = {Journal of Computing and Information Science in Engineering},
        month = mar,
        number = {2},
        pages = {021009+},
        title = {Analysis of Collaborative Design Networks: A Case Study of {OpenIDEO}},
        url = {http://dx.doi.org/10.1115/1.4026510},
        volume = {14},
        year = {2014}
    }

Mark Fuge, Alice Agogino. "How Online Design Communities Evolve Over Time: the Birth and Growth of OpenIDEO," in Proceedings of ASME 2014 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference, August 17-20, 2014, Buffalo, USA.

    @inproceedings{fuge:openideo_evolution_IDETC_2014,
        author = {Mark Fuge and Alice Agogino},
        title = {How Online Design Communities Evolve Over Time: the Birth and Growth of {OpenIDEO}},
        booktitle = {ASME International Design Engineering Technical Conferences},
        year = {2014},
        month = {August},
        location = {Buffalo, USA},
        publisher = {ASME}
    }
    

    
The any code is licensed under the Apache v2 license. 
    
Usage
-----

As an example of how to use our data in your own research, you can access the concept and social graphs using the following example. It assumes that you have placed the data in a default "graph_data" folder (though this can be changed by passing an argument into load_challenge):
  
    from graph2 import *
    challenge = load_challenge(7)
    # The concept graph is a NetworkX object with concepts as nodes
    # and "built upon" citations as directed edges
    challenge.concept_graph
    # The social graph is a NetworkX object with users as nodes
    # and "communication" actions as directed edges
    challenge.social_graph
    # The link attribute points you to the original challenge site
    challenge.link

