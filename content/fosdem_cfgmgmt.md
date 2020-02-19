Title: Trip report for FOSDEM and cfgmgmtcamp 2020
Date: 2020-02-19 12:03
Modified: 2016-02-19 12:03
Category: conference
Tags: open source, ansible, automation, trip report
Slug: fosdem-cfgmgmt
Authors: Abhijeet Kasurde
Summary: A Trip report for FOSDEM and cfgmgmtcamp 2020


I recently attended [FOSDEM 2020](https://fosdem.org/2020) in Brussels, Belgium and [Cfgmgmtcamp 2020](https://cfgmgmtcamp.eu/ghent2020/) in Ghent, Belgium. The following is a trip report for the same.

This all started with a long weekend of conference and beer club hoping. I arrived in Brussels a night before the conference and went to the huge beer party organized in [Delirium Cafe](https://www.deliriumvillage.com/bar/delirium-cafe/) by FOSDEM organizers.

![Beer]({filename}/images/fosdem/beer_1.jpg)

It was fun and surprising to attend a beer party organized by an event organizer. The room was full of geeks passionate about open source and community enjoying more than 2000 different beers under one roof.


![FOSDEM 2020 - Welcome]({filename}/images/fosdem/fosdem_1.jpg)

The next morning the conference kicked at [ULB](https://www.ulb.be/en) with a keynote speaker ["Thorsten Leemhuis"](https://fosdem.org/2020/schedule/speaker/thorsten_leemhuis/). He talked about ["The Linux Kernel: We have to finish this thing one day ;)Solving big problems in small steps for more than two decades"](https://fosdem.org/2020/schedule/event/linux_kernel/).

![ULB]({filename}/images/fosdem/ulb_1.jpg)

After the welcome and first keynote session, I attended ["Using OpenAPI to Maximise Your Pulp 3 Experience"](https://fosdem.org/2020/schedule/event/openapi/) where ["Dennis Kliban"](https://fosdem.org/2020/schedule/speaker/dennis_kliban/) talked about latest Pulp OpenAPI interface and how user can use it.

Next talk was interesting and was related to Ansible - [Doomed are the dinosaurs!](https://fosdem.org/2020/schedule/event/doomed/) by [David Heijkamp](https://fosdem.org/2020/schedule/speaker/david_heijkamp/), where he talked about diversity about the utilization of the various open source projects and Ansible. Happy to see when speaker mentioned ["Ansible in the center"](https://twitter.com/Pyro46/status/1223557781078319104?s=20).

Next, my friend [Amit Upadhye](https://fosdem.org/2020/schedule/speaker/amit_upadhye/) presented ["Compliance management with OpenSCAP and Ansible"](https://fosdem.org/2020/schedule/event/openscap/).He showed how organization can use OpenSCAP and Ansible to automate their compliance management tasks with ease.

[Ganesh](https://fosdem.org/2020/schedule/speaker/ganesh_nalawade/) and [I](https://fosdem.org/2020/schedule/speaker/abhijeet_kasurde/) were next in the line to present in the "Infra managment devroom". We presented the future of Ansible content packaging and distribution i.e. "Collection". You can find the link of our talk and collection demo [here](https://fosdem.org/2020/schedule/event/ansible_collections/). People were excited and interested to know more about the Ansible collections.

After this I took a lunch break, then attended ["Foreman meets Ansible"] by ["Adam Růžička"](https://fosdem.org/2020/schedule/speaker/adam_ruzicka/). He spoke about Foreman allows user to plug Ansible in its architecture. The next session was ["Hacking Terraform for fun and profit"](https://fosdem.org/2020/schedule/event/terraform/) by [Anton Babenko](https://fosdem.org/2020/schedule/speaker/anton_babenko/).

I saw a lot of speaker talking about "YAML" in their talks. Some of them were pro-YAML and some of them were not liking YAML at all. It was interesting to see the reasoning for introduction of new DSL in configuration management tools.

Next session was related to configuration management software called ["Pulumi"](https://www.pulumi.com/), which treats infrastructure as a code. I never heard about this software before and was interesting know about. [Paul Stack](Paul Stack) talked about ["Infrastructure testing, it's a real thing!"](https://fosdem.org/2020/schedule/event/infratesting/) using Pulumi.

Then I attended [Mgmt Config: Autonomous Datacentres](https://fosdem.org/2020/schedule/event/mgmt/) by [James Shubin](https://fosdem.org/2020/schedule/speaker/james_shubin/) who started his talk literally using Hip-Hop song which was initiated by command line terminal. The whole conf room was turned into a club for next 5 minutes. James talked about MgmtConfig by providing various examples which showed how MgmtConfig can be used in real time and autonomous way to do the automation. It was fun to attend lightweight and but still engaging talk to end the day.

After this session, I headed towards a hallway where all community booths were located. There I met several people and had a brief intro session with them. We talked about Ansible, YAML, the future of VMware automation in Ansible etc.,
I had a chances to meet couple of folks from Ansible IRC channel and GitHub community. I really love the appreciation from the community members.

I spent most of Saturday in Infra room as I was keen to know more about infra related stuff.
But I had different agenda for Sunday. I wanted to attend various talks related to RUST and Golang but end up spending most of the time in Go Language devroom. This was managed by Google folks.

Sunday morning, started with me attending [Vitaly Kuznetsov](https://fosdem.org/2020/schedule/speaker/vitaly_kuznetsov/) talk about ["Public clouds and vulnerable CPUs: are we secure?"](https://fosdem.org/2020/schedule/event/vai_pubic_clouds_and_vulnerable_cpus/). He talked about various CPU vulnerabilities and how they affect Public cloud offering and how user can mitigate them. It was interesting to know a lot of vulnerabilities are out there in the wild and their detection and mitigation.

Next session in Virtualization and IaaS devroom, was [virtio-fs](https://fosdem.org/2020/schedule/event/vai_virtio_fs/) by [Stefan Hajnoczi](https://fosdem.org/2020/schedule/speaker/stefan_hajnoczi/). He talked about shared file system for the virtual machines and its implementation. After that I attended [io_uring in QEMU: high-performance disk I/O for Linux](https://fosdem.org/2020/schedule/event/vai_io_uring_in_qemu/) by [Julia Suvorova](https://fosdem.org/2020/schedule/speaker/julia_suvorova/). Author talked about new feature of Linux Kernel called "io_uring" and its implementation in QEMU.

After this I headed towards "Go devroom" since the talk line up there was awesome. I attend three talks back-to-back [Advanced debugging techniques of Go code](https://fosdem.org/2020/schedule/event/advanceddebugginggo/) by [Andrii Soldatenko](https://fosdem.org/2020/schedule/speaker/andrii_soldatenko/), [Debug code generation in Go](https://fosdem.org/2020/schedule/event/debugcodegenerationgo/) by [Jaana Dogan](https://fosdem.org/2020/schedule/speaker/jaana_dogan/) and [Uplift your Linux systems programming skills with systemd and D-Bus](https://fosdem.org/2020/schedule/event/golinux/) by [Leonid Vasilyev](https://fosdem.org/2020/schedule/speaker/leonid_vasilyev/). All of these talks were very informative and lived up to my expectations.

Thanks for FOSDEM organizers we can watch every talk since everything is recorded and can be found [here](https://fosdem.org/2020/schedule/events/). I will go through all sessions which I missed while I attending some other talks.

I would like to thank [Carol Chen](https://twitter.com/cybette) and [gundalow](https://twitter.com/the_gundalow) who helped us to get the opportunity to talk in such a big Open Source event.

This ends the part one of conference hoping. Next conference in the line was [cfgmgmtcamp 2020](https://cfgmgmtcamp.eu/ghent2020/) which was organized in [Ghent, Belgium](https://en.wikipedia.org/wiki/Ghent). This city is scenic and beautiful, still maintaining its heritage with cathedrals and historical monuments. I would definitely recommend people to visit this beautiful city at least once in their lifetime.


Conference was organized in the [Hogeschool Gent](https://en.wikipedia.org/wiki/Hogeschool_Gent).

![hogent]({filename}/images/fosdem/ho_gent.jpg)

We started Ansible community booth in the common area of the conference. I attended keynote [Untitled Config Game](https://cfp.cfgmgmtcamp.be/2020/talk/VQRGFB/) by [Ryn Daniels](https://cfp.cfgmgmtcamp.be/2020/speaker/QXJSAH/), speaker talked about their experience in DevOps role by providing various illustration of Goose. Talk was awesome and inspiring. You can check out picture of the full house [here](https://twitter.com/PeetersSimon/status/1224256018105978885?s=20).

![Untitled]({filename}/images/fosdem/untitled_1.jpg)

[gundalow](https://twitter.com/the_gundalow) and I started in Ansible room and helping speakers and ushering in the room. Since the room was allocated to Ansible, all talks were related to use cases, customer scenarios and problem solution using Ansible. First session was [Maintaining over 40 Ansible modules: 4 years later](https://cfp.cfgmgmtcamp.be/2020/talk/U7CGMZ/) by [Evgeni Golov](https://cfp.cfgmgmtcamp.be/2020/speaker/JZ937Y/) where speaker talked about their experience about Ansible and Foreman modules.

Next session was [Ansible Collaboration within your Organization](https://cfp.cfgmgmtcamp.be/2020/talk/KSEFVV/) by [Brian Bouterse](https://cfp.cfgmgmtcamp.be/2020/speaker/MBJSKS/) and [Oleksandr Saprykin](https://cfp.cfgmgmtcamp.be/2020/speaker/WKJMUJ/) where we learned about Ansible collaboration within organization using example use case of Galaxy and [pulp_ansible](https://pulp-ansible.readthedocs.io/) teams.

Next talk was very interesting where [Eric Kellar](https://cfp.cfgmgmtcamp.be/2020/speaker/HMXQ7K/) talked about their use case using [Global Linux client with Ansible and Foreman](https://cfp.cfgmgmtcamp.be/2020/talk/QNSP9S/). Speaker told us about changing minds about how automation can bring value to our organisation.

During the dinner party organized by cfgmgmtcamp organizer, we got chance to sit across people from different companies like [cfengine](https://cfengine.com/) and [Puppet](https://puppet.com/). We discussed about various topics like YAML's pros and cons, architecture details about cfengine and puppet, Puppet Bolt vs Ansible, Agentless vs Agentful architecture.
It was fun and engaging discussion which shows true spirit of Open source software where people discuss anything and everything.

Second day started with keynote by [Michael Ducy](https://cfp.cfgmgmtcamp.be/2020/speaker/9BEFDC/) where speaker explained about [Automating Security Response with Serverless](https://cfp.cfgmgmtcamp.be/2020/talk/YD8UGG/) with various open source tools. It gave us a fresh prespective about how to leverage Serverless based automation in their operational roles.

I took a picture in this talk and it was apt to situation from the movie "Matrix"

![matrix]({filename}/images/fosdem/matrix_1.jpg)

Then I attended a [talk](https://cfp.cfgmgmtcamp.be/2020/talk/AMU8TP/) by [Matthias Dellweg](https://cfp.cfgmgmtcamp.be/2020/speaker/EPWQGN/) and [Bernhard Hopfenmüller](https://cfp.cfgmgmtcamp.be/2020/speaker/MPEXML/) who talked about importance of testing in software development lifecycle. In this talk they provided an insight into Molecule usage and discuss the possibilities and challenges that it brings.

![molecule]({filename}/images/fosdem/cfg_2.jpg)


On the last day of conference, we had a workshop for Ansible [Writing Ansible Modules for fun and profit](https://cfp.cfgmgmtcamp.be/2020/talk/HH9T93/). This workshop is helpful for developers and system administrators with some knowledge of Python to develop their custom modules and contribute back to the community. In this workshop, we covered Ansible Module Architecture, Ansible development environment, Ansible Module development, Ansible Contribution process etc., Even though this was the last workshop of the conference, we had a roomful of Ansible enthusiasts and attendees.

I enjoyed a lot during this visit and will definitely come back next year to attend both conferences. Hope to see you soon in these conference.