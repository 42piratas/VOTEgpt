export interface Candidate {
  image: string;
  name: string;
  age: number;
  born: string;
  education: string;
  partyCurrent: string;
  links: Links[];
  keyworkds: string[];
  partyPrevious: string;
  simpleDescription: string;
  bio: string;
  description: string;
  nothoriousFor: string;
  platform: string;
  endorsements: string;
  foundingSources: string;
  previewsPoliticalExperience: string;
  criminalHistory: string;
}

export interface Links {
  wikipedia: string;
  website: string;
  social: string;
}
