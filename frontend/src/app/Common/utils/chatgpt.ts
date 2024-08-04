import OpenAI from 'openai';
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});
async function mainOpenAI(prompt: string) {
  const completion = await openai.chat.completions.create({
    messages: [
      {
        role: 'system',
        content: prompt,
      },
    ],
    model: 'gpt-4o-mini',
  });
  return completion.choices[0].message.content;
}

export default mainOpenAI;
