# Installing Typescript

You can install TypeScript **globally** to have access to it from any directory.

```
npm install -g typescript
```

You can install TypeScript **locally** and save to package.json to restrict to a directory.

```
npm install typescript --save-dev
```

## Compiling TypeScript code

The *tsc* compilation command comes with typescript, which can be used to compile code.

```
tsc my-code.ts
```

This creates a *my-code.js* file.

## Running TypeScript using ts-node

**ts-node** is an npm package which allows the user to run typescript files directly, without the need for
precompilation using tsc. It also provides REPL.

Install ts-node globally using.

```
npm install -g ts-node
```

Once installed it´s possible to execute typescript code without compiling.

```
ts-node sample.ts
```
