from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List, Optional


@dataclass_json
@dataclass
class CV:
    personal_information: Optional['PersonalInformation'] = None
    education: Optional[List['Education']] = None
    work_experience: Optional[List['WorkExperience']] = None
    skills: Optional[List[str]] = None
    certifications: Optional[List['Certification']] = None
    languages: Optional[List['Language']] = None
    hobbies: Optional[List[str]] = None


@dataclass_json
@dataclass
class Certification:
    name: Optional[str] = None
    issuing_organization: Optional[str] = None
    issue_date: Optional[str] = None


@dataclass_json
@dataclass
class PersonalInformation:
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None


@dataclass_json
@dataclass
class Education:
    institution: Optional[str] = None
    degree: Optional[str] = None
    field_of_study: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None


@dataclass_json
@dataclass
class WorkExperience:
    company: Optional[str] = None
    position: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    responsibilities: Optional[List[str]] = None


@dataclass_json
@dataclass
class Certification:
    name: Optional[str] = None
    issuing_organization: Optional[str] = None
    issue_date: Optional[str] = None


@dataclass_json
@dataclass
class Language:
    name: Optional[str] = None
    proficiency: Optional[str] = None
