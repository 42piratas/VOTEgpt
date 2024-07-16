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

export interface Bio {
  id: number;
  image: string;
  name: string;
  age: number;
  birth: BirthInfo;
  education: string;
  party: PartyInfo;
  online: OnlinePresence;
  keywords: string[];
  bio: string;
  notoriousFor: string[];
  // platform: Platform;
  platform: string;
  endorsements: string[];
  fundingSources: string[];
  previousPoliticalExperience: string;
  criminalRecords: string[];
  policies: Policies;
}
interface BirthInfo {
  year: number;
  place: string;
}

interface PartyInfo {
  current: string;
  since: number;
  previous: string;
}

interface OnlinePresence {
  wikipedia: string;
  officialWebsite: string;
  truthSocial: string;
}

interface Platform {
  taxCuts: boolean;
  deregulation: boolean;
  borderWall: boolean;
  strictImmigrationPolicies: boolean;
  renegotiatingTradeDeals: boolean;
  repealObamacare: boolean;
  americaFirst: boolean;
}

interface Policies {
  abortion: string;
  healthcare: string;
  economy: string;
  immigration: string;
  gunControl: string;
  climateChange: string;
  education: string;
  taxes: string;
  lgbtqRights: string;
  foreignPolicy: string;
  drugPolicy: string;
  criminalJusticeReform: string;
  militarySpending: string;
  votingRights: string;
}

export interface Links {
  wikipedia: string;
  website: string;
  social: string;
}
