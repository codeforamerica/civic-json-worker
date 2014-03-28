import factory
from app import Organization, Project, Event, Story, db
from factory.alchemy import SQLAlchemyModelFactory
from sqlalchemy.orm import scoped_session, sessionmaker
from random import choice
from datetime import datetime, timedelta

class OrganizationFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Organization
    FACTORY_SESSION = db.session

    name = factory.Sequence(lambda n: 'Civic Organization {0}'.format(n))
    website = factory.Sequence(lambda n: 'http://www.civicorganization{0}.com'.format(n))
    events_url = factory.Sequence(lambda n: 'http://www.meetup.com.com/events/civicproject{0}'.format(n))
    rss = factory.Sequence(lambda n: 'http://www.civicorganization{0}.rss'.format(n))
    projects_list_url = factory.Sequence(lambda n: 'http://www.civicorganization{0}.com/projects'.format(n))
    city = "San Francisco, CA"
    latitude = 37.7749
    longitude = -122.4194
    type = "Brigade"

class ProjectFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Project
    FACTORY_SESSION = db.session

    name = 'Civic Project'
    code_url = 'http://www.github.com/civic-project'
    link_url = 'http://www.civicproject.com'
    description = 'This is a description'
    type = factory.LazyAttribute(lambda n: choice(['web service', 'api', 'data standard']))
    categories = factory.LazyAttribute(lambda n: choice(['housing', 'community engagement', 'criminal justice', 'education']))
    github_details = {'repo': 'git@github.com:codeforamerica/civic-project.git'}
    organization_name = factory.LazyAttribute(lambda e: OrganizationFactory().name)


class EventFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Event
    FACTORY_SESSION = db.session
    FACTORY_HIDDEN_ARGS = ('now',)

    name = factory.Sequence(lambda n: 'Civic Event {0}'.format(n))
    description = 'A civic event'
    event_url = factory.Sequence(lambda n: 'http://www.meetup.com/civic-project-hack-night{0}'.format(n))
    location = '155 9th St., San Francisco, CA'

    now = factory.LazyAttribute(lambda o: datetime.utcnow())
    start_time = factory.LazyAttribute(lambda o: o.now + timedelta(hours=10))
    end_time = factory.LazyAttribute(lambda o: o.now + timedelta(hours=12))
    created_at = factory.LazyAttribute(lambda o: o.now)
    organization_name = factory.LazyAttribute(lambda e: OrganizationFactory().name)

class StoryFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Story
    FACTORY_SESSION = db.session

    title = factory.Sequence(lambda n: 'Civic Story {0}'.format(n))
    link = 'http://www.codeforamerica.org/blog/2014/03/19/thanks-again-for-your-support-esri/'
    type = "blog"
    organization_name = factory.LazyAttribute(lambda e: OrganizationFactory().name)