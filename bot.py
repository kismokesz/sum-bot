module.exports = (client) => {
  client.on('interactionCreate', async (interaction) => {
    if (!interaction.isChatInputCommand()) return;
    if (interaction.commandName !== 'cal') return;

    const channel = interaction.channel;

    await interaction.reply(':1234: Számolok...');

    const messages = await channel.messages.fetch({ limit: 100 });

    let sum = 0;
    let count = 0;

    messages.forEach(msg => {
      // Mentions és csatorna hivatkozások eltávolítása mielőtt számokat keresünk
      const cleaned = msg.content
        .replace(/<@!?\d+>/g, '')   // user mention
        .replace(/<#\d+>/g, '')     // csatorna mention
        .replace(/<@&\d+>/g, '');   // role mention

      const numbers = cleaned.match(/-?\d+(\.\d+)?/g);
      if (numbers) {
        numbers.forEach(n => {
          sum += parseFloat(n);
          count++;
        });
      }
    });

    await interaction.editReply(
      `✅ **Összesítés**\n` +
      `📊 Talált számok: **${count} db**\n` +
      `➕ Összeg: **${sum}**`
    );
  });
};
