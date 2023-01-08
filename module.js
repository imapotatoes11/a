import { Configuration, OpenAIApi } from "openai";
const configuration = new Configuration({
    organization: "org-QFPtmDLZfL9bB3MDtnsooLcF",
    apiKey: "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",
});
export const openai = new OpenAIApi(configuration);
const response = await openai.listEngines();
export async function OAIResponse(openai) {
    /*fetch('https://api.openai.com/v1/completions',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization':'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'
        },
        body:JSON.stringify({
            model:'text-davinci-003',
            prompt:'Say this is a test',
            temperature:0.9,
            max_tokens:500
        })
    })
        .then(response=>response.json())
        .then(data=>console.log(data))
        .catch(error=>console.log(error));*/
    const completion = await openai.createCompletion({
        model: "text-davinci-003",
        prompt: "Say this is a test",
        temperature: 0.9,
    })
    console.log(completion)
    console.log(completion.data)
}