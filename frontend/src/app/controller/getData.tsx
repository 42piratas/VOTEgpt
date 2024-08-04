import axios from 'axios';

const API_URL = process.env.API_URL;
const CountriesData = async () => {
  const response = await axios.get(`${API_URL}/countries`);
  const data = response.data;
  return data;
};

const DemocracyIndex = async (country: string) => {
  const response = await axios.get(`${API_URL}/democracy/${country}`);
  const data = response.data;
  return data;
};

const ElectionData = async (country: string) => {
  const isDemocratic = await DemocracyIndex(country);
  if (!isDemocratic[0]) return;
  const response = await axios.get(`${API_URL}/elections/${country}`);
  const data = response.data;

  return {
    isDemocratic: isDemocratic[0],
    elections: data,
  };
};

const CandidateByCountryAndElection = async (
  country: string,
  election: string,
  election_date: string
) => {
  const response = await axios.get(
    `${API_URL}/candidates/${country}/${election}/${election_date}`
  );
  const data = response.data;
  console.log(data);
  return data;
};

export const electionsController = {
  CountriesData,
  DemocracyIndex,
  ElectionData,
  CandidateByCountryAndElection,
};
