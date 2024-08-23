FROM python:3.8-alpine  as builder
WORKDIR /
RUN mkdir builder
WORKDIR /builder
RUN mkdir icons
COPY builder.py .
COPY App.tsx.tmp .
COPY icons-tool-util.tsx.tmp .
COPY icons/*.svg icons
RUN pip install jinja2
RUN python builder.py

FROM node:21-alpine  as runner
RUN apk add --no-cache git
WORKDIR /
RUN npm create vite@latest test -- --template react-ts
WORKDIR /test
COPY --from=builder /builder/App.tsx /test/src/App.tsx
COPY --from=builder /builder/icons-tool-util.tsx /test/src/icons-tool-util.tsx
COPY index.css /test/src/index.css
COPY index.html /test/index.html
COPY favicon.svg /test/favicon.svg
COPY icons/*.svg /test/
RUN npm install
RUN npm install tldraw

ENV SHELL /bin/sh
ENV HOST 0.0.0.0
EXPOSE 5173
CMD [ "npm", "run", "dev", "--", "--host" ]
